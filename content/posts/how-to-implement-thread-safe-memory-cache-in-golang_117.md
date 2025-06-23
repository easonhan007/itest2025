---
weight: 1
title: "如何实现线程安全的内存缓存"
date: 2024-03-08T09:04:31+08:00
lastmod: 2024-03-08T09:04:31+08:00
draft: false
author: "乙醇"
authorLink: "https://github.com/easonhan007"
description: "一个用go实现的线程安全的内存缓存，实现代码非常简洁高效，不卖弄不烧脑"
images: []
resources:
  - name: "featured-image"
    src: "https://images.unsplash.com/photo-1542903660-eedba2cda473?w=300"

tags: []
categories: ["测试工具", "软件测试基础"]

lightgallery: true

toc:
  auto: false
---

这两天正好看到一个用 go 实现的线程安全的内存缓存，实现代码非常简洁高效，不卖弄不烧脑，非常值得初学者拿来学习。

### 项目地址

项目地址在[https://github.com/muesli/cache2go](https://github.com/muesli/cache2go)，目前已经有 1.8k 的 star。

### 如何使用

```go
package main

import (
	"github.com/muesli/cache2go"
	"fmt"
	"time"
)

// Keys & values in cache2go can be of arbitrary types, e.g. a struct.
type myStruct struct {
	text     string
	moreData []byte
}

func main() {
	// Accessing a new cache table for the first time will create it.
	cache :=

	// We will put a new item in the cache. It will expire after
	// not being accessed via Value(key) for more than 5 seconds.
	val := myStruct{"This is a test!", []byte{}}
	cache.Add("someKey", 5*time.Second, &val)

	// Let's retrieve the item from the cache.
	res, err := cache.Value("someKey")
	if err == nil {
		fmt.Println("Found value in cache:", res.Data().(*myStruct).text)
	} else {
		fmt.Println("Error retrieving value from cache:", err)
	}

	// Wait for the item to expire in cache.
	time.Sleep(6 * time.Second)
	res, err = cache.Value("someKey")
	if err != nil {
		fmt.Println("Item is not cached (anymore).")
	}

	// Add another item that never expires.
	cache.Add("someKey", 0, &val)

	// cache2go supports a few handy callbacks and loading mechanisms.
	cache.SetAboutToDeleteItemCallback(func(e *cache2go.CacheItem) {
		fmt.Println("Deleting:", e.Key(), e.Data().(*myStruct).text, e.CreatedOn())
	})

	// Remove the item from the cache.
	cache.Delete("someKey")

	// And wipe the entire cache table.
	cache.Flush()
}
```

简单看一下核心 api

- 创建缓存对象: `cache2go.Cache("myCache")`
- 设置一个 key:value 对：`cache.Add("someKey", 5*time.Second, &val)` 设置的时候需要指定缓存的过期时间
- 获取 key 对应的 value 值: `res, err = cache.Value("someKey")`

这里就简单分析一下对应接口的实现原理。

### key value 存储

这里使用的是 CacheItem 这个结构体来实现的 key value 存储。相应的数据结构是

```go
// CacheItem is an individual cache item
// Parameter data contains the user-set value in the cache.
type CacheItem struct {
	sync.RWMutex

	// The item's key.
	key interface{}
	// The item's data.
	data interface{}
	// How long will the item live in the cache when not being accessed/kept alive.
	lifeSpan time.Duration

	// Creation timestamp.
	createdOn time.Time
	// Last access timestamp.
	accessedOn time.Time
	// How often the item was accessed.
	accessCount int64

	// Callback method triggered right before removing the item from the cache
	aboutToExpire []func(key interface{})
}
```

值得注意的点有

- 读写锁: `sync.RWMutex` 多线程访问的时候用来进行资源的排他锁定
- 键的实现: `key interface{}` 所以 key 可以是任意类型
- 值的实现: `data interface{}` 跟 key 类似，value 可以是任意类型
- 存活时间: `lifeSpan time.Duration` 大于这个时间间隔没有被访问的话，的话 key 就会过期被清理
- 上次被访问的时间: `accessedOn time.Time`
- key 被访问的次数: `accessCount`

再看一下 CacheItem 初始化的代码

```go
// NewCacheItem returns a newly created CacheItem.
// Parameter key is the item's cache-key.
// Parameter lifeSpan determines after which time period without an access the item
// will get removed from the cache.
// Parameter data is the item's value.
func NewCacheItem(key interface{}, lifeSpan time.Duration, data interface{}) *CacheItem {
	t := time.Now()
	return &CacheItem{
		key:           key,
		lifeSpan:      lifeSpan,
		createdOn:     t,
		accessedOn:    t,
		accessCount:   0,
		aboutToExpire: nil,
		data:          data,
	}
}
```

可以看出来创建时间和上次访问时间都被设置成了当前时间，访问次数是 0.

### 缓存对象的实现 CacheTable

CacheTable 对象包含了 n 个 CacheItem，看一下具体的数据结构

```go
type CacheTable struct {
	sync.RWMutex

	// The table's name.
	name string
	// All cached items.
	items map[interface{}]*CacheItem

	// Timer responsible for triggering cleanup.
	cleanupTimer *time.Timer
	// Current timer duration.
	cleanupInterval time.Duration

	// The logger used for this table.
	logger *log.Logger

	// Callback method triggered when trying to load a non-existing key.
	loadData func(key interface{}, args ...interface{}) *CacheItem
	// Callback method triggered when adding a new item to the cache.
	addedItem []func(item *CacheItem)
	// Callback method triggered before deleting an item from the cache.
	aboutToDeleteItem []func(item *CacheItem)
}
```

这里需要关注的地方是

- `items map[interface{}]*CacheItem` : 每个 item 其实都是这个 map 里的一项，其实 map 的 key 就是 item 的 key
- `cleanupTimer *time.Timer` : 用来做缓存过期的定时器
- `cleanupInterval time.Duration` ： 扫描所有的 items 进行缓存过期清理的时间间隔

### 添加一个 key value

```go
// Add adds a key/value pair to the cache.
// Parameter key is the item's cache-key.
// Parameter lifeSpan determines after which time period without an access the item
// will get removed from the cache.
// Parameter data is the item's value.
func (table *CacheTable) Add(key interface{}, lifeSpan time.Duration, data interface{}) *CacheItem {
	item := NewCacheItem(key, lifeSpan, data)

	// Add item to cache.
	table.Lock()
	table.addInternal(item)

	return item
}

func (table *CacheTable) addInternal(item *CacheItem) {
	// Careful: do not run this method unless the table-mutex is locked!
	// It will unlock it for the caller before running the callbacks and checks
	table.log("Adding item with key", item.key, "and lifespan of", item.lifeSpan, "to table", table.name)
	table.items[item.key] = item

	// Cache values so we don't keep blocking the mutex.
	expDur := table.cleanupInterval
	addedItem := table.addedItem
	table.Unlock()

	// Trigger callback after adding an item to cache.
	if addedItem != nil {
		for _, callback := range addedItem {
			callback(item)
		}
	}

	// If we haven't set up any expiration check timer or found a more imminent item.
	if item.lifeSpan > 0 && (expDur == 0 || item.lifeSpan < expDur) {
		table.expirationCheck()
	}
}
```

梳理一下流程

- 创建 cache item
- 加读写锁
- 调用`addInternal` 方法
- 在 items map 里添加一项，key 就是 item 的 key，value 就是 item
- 获取整个 CacheTable 的清理缓存间隔时间
- 解锁，到这一步基本上就完成了数据的持久化
- 运行添加 item 时的回调函数，如果有的话
- 如果 item 设置了过期时间，并且 table 的过期扫描间隔是 0（首次添加）或者 item 的过期间隔小于 table 的过期间隔时间的话，调用`expirationCheck` 函数，进行过期扫描

### 扫描并清理过期的 key

代码如下

```go
// Expiration check loop, triggered by a self-adjusting timer.
func (table *CacheTable) expirationCheck() {
	table.Lock()
	if table.cleanupTimer != nil {
		table.cleanupTimer.Stop()
	}
	if table.cleanupInterval > 0 {
		table.log("Expiration check triggered after", table.cleanupInterval, "for table", table.name)
	} else {
		table.log("Expiration check installed for table", table.name)
	}

	// To be more accurate with timers, we would need to update 'now' on every
	// loop iteration. Not sure it's really efficient though.
	now := time.Now()
	smallestDuration := 0 * time.Second
	for key, item := range table.items {
		// Cache values so we don't keep blocking the mutex.
		item.RLock()
		lifeSpan := item.lifeSpan
		accessedOn := item.accessedOn
		item.RUnlock()

		if lifeSpan == 0 {
			continue
		}
		if now.Sub(accessedOn) >= lifeSpan {
			// Item has excessed its lifespan.
			table.deleteInternal(key)
		} else {
			// Find the item chronologically closest to its end-of-lifespan.
			if smallestDuration == 0 || lifeSpan-now.Sub(accessedOn) < smallestDuration {
				smallestDuration = lifeSpan - now.Sub(accessedOn)
			}
		}
	}

	// Setup the interval for the next cleanup run.
	table.cleanupInterval = smallestDuration
	if smallestDuration > 0 {
		table.cleanupTimer = time.AfterFunc(smallestDuration, func() {
			go table.expirationCheck()
		})
	}
	table.Unlock()
}
```

简单过一起逻辑

- 加读写锁
- 如果启动了扫描定时器，关闭定时器先
- 扫描所有的 key，对每一个 key
  - 加读锁
  - 获取 key 的存活周期
  - 获取 key 的上次访问时间
  - 如果存活周期是 0，则不处理，这是持续保活的逻辑，可以先不管
  - 如果现在的时间距离上次访问时间已经大于了 key 的存活时间，则删除这个 key
  - 否则的话算出所有 key 里面最快要到期的那个 key 的时间间隔
- 如果有拿到了最快要到期那个 key 的时间间隔，则运行定时器，在下这个时间间隔之后运行清理函数
- 解锁

### 删除 key 的实现

```go
// Delete an item from the cache.
func (table *CacheTable) Delete(key interface{}) (*CacheItem, error) {
	table.Lock()
	defer table.Unlock()

	return table.deleteInternal(key)
}

func (table *CacheTable) deleteInternal(key interface{}) (*CacheItem, error) {
	r, ok := table.items[key]
	if !ok {
		return nil, ErrKeyNotFound
	}

	// Cache value so we don't keep blocking the mutex.
	aboutToDeleteItem := table.aboutToDeleteItem
	table.Unlock()

	// Trigger callbacks before deleting an item from cache.
	if aboutToDeleteItem != nil {
		for _, callback := range aboutToDeleteItem {
			callback(r)
		}
	}

	r.RLock()
	defer r.RUnlock()
	if r.aboutToExpire != nil {
		for _, callback := range r.aboutToExpire {
			callback(key)
		}
	}

	table.Lock()
	table.log("Deleting item with key", key, "created on", r.createdOn, "and hit", r.accessCount, "times from table", table.name)
	delete(table.items, key)

	return r, nil
}
```

删除的逻辑相对简单一些，主要是需要注意加锁解锁以及运行之前注册的回调函数。

### 总结

这应该是我见过代码最简单但是 star 相对比较多的开源项目了。这个项目非常适合我们进行学习，因为

- 可以帮助我们理解锁的使用以及如何使用锁来保证线程安全；
- 帮助我们理解 key value 内存缓存的实现
- 提供了一种使用定时器来实现定时任务的思路
- 帮助我们理解如何注册和运行回调函数
