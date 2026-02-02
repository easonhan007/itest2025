package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strings"
	"time"
)

func printHelp() {
	help := `cr - Hugo 周刊文章目录创建工具

用法:
  cr <directory-name>
  cr -h, --help

参数:
  <directory-name>    要在 content/posts/ 下创建的目录名称
                      例如: weekly_02, testing_weekly_003

选项:
  -h, --help         显示此帮助信息

功能:
  1. 在 content/posts/ 下创建指定目录
  2. 自动查找 content/posts/ 目录下最新的 .md 文件
  3. 复制该文件的 front matter 结构
  4. 保留 date 字段的值，清空其他字段的值
  5. 在该目录下创建 index.md

示例:
  # 创建 weekly_02 目录
  ./cr weekly_02

  # 显示帮助
  ./cr --help

输出示例:
  Created content/posts/weekly_02/index.md

注意事项:
  - 工具会从 content/posts/ 目录下所有 .md 文件中选择最新修改的文件
  - 如果找不到 front matter，会使用默认模板
  - 已存在的目录不会被覆盖，index.md 会被更新
`
	fmt.Println(help)
}

func main() {
	if len(os.Args) < 2 {
		printHelp()
		os.Exit(1)
	}

	if os.Args[1] == "-h" || os.Args[1] == "--help" {
		printHelp()
		os.Exit(0)
	}

	dirName := os.Args[1]
	postsDir := "../content/posts"

	// Find the newest .md file
	newestFile, err := findNewestMarkdownFile(postsDir)
	if err != nil {
		fmt.Printf("Error finding newest file: %v\n", err)
		os.Exit(1)
	}

	// Read the file
	content, err := os.ReadFile(newestFile)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		os.Exit(1)
	}

	// Extract and process front matter
	frontMatter := extractAndProcessFrontMatter(string(content))

	// Create directory
	newDir := filepath.Join(postsDir, dirName)
	if err := os.MkdirAll(newDir, 0755); err != nil {
		fmt.Printf("Error creating directory: %v\n", err)
		os.Exit(1)
	}

	// Create index.md with processed front matter
	indexPath := filepath.Join(newDir, "index.md")
	if err := os.WriteFile(indexPath, []byte(frontMatter), 0644); err != nil {
		fmt.Printf("Error writing index.md: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Created %s\n", indexPath)
}

func findNewestMarkdownFile(dir string) (string, error) {
	var files []string
	var modTimes []time.Time

	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && strings.HasSuffix(info.Name(), ".md") {
			files = append(files, path)
			modTimes = append(modTimes, info.ModTime())
		}
		return nil
	})

	if err != nil {
		return "", err
	}

	if len(files) == 0 {
		return "", fmt.Errorf("no markdown files found")
	}

	// Sort by modification time (newest first)
	sort.Slice(files, func(i, j int) bool {
		return modTimes[i].After(modTimes[j])
	})

	return files[0], nil
}

func extractAndProcessFrontMatter(content string) string {
	// Normalize line endings to Unix-style
	content = strings.ReplaceAll(content, "\r\n", "\n")

	// Try YAML format (---)
	yamlRe := regexp.MustCompile(`(?s)^---\n(.*?)\n---`)
	matches := yamlRe.FindStringSubmatch(content)
	isTOML := false

	// If no YAML front matter, try TOML format (+++)
	if len(matches) < 2 {
		tomlRe := regexp.MustCompile(`(?s)^\+\+\+\n(.*?)\n\+\+\+`)
		matches = tomlRe.FindStringSubmatch(content)
		isTOML = true
	}

	if len(matches) < 2 {
		// No front matter found, return default template with current date
		date := time.Now().Format("2006-01-02T15:04:05+08:00")
		return fmt.Sprintf("---\ndate: %s\n---\n\n", date)
	}

	frontMatter := matches[1]

	// Parse all key-value pairs
	var keys []string
	keyValues := make(map[string]string)

	lines := strings.Split(frontMatter, "\n")
	var currentKey string
	var currentValueLines []string
	inMultiline := false

	for _, line := range lines {
		trimmed := strings.TrimSpace(line)

		// Skip empty lines (but preserve them in multiline values)
		if trimmed == "" {
			if inMultiline && currentKey != "" {
				currentValueLines = append(currentValueLines, "")
			}
			continue
		}

		// Skip nested/child lines (lines starting with whitespace)
		// These are part of parent key's value structure
		if len(line) > 0 && (line[0] == ' ' || line[0] == '\t') {
			if inMultiline && currentKey != "" {
				currentValueLines = append(currentValueLines, line)
			}
			continue
		}

		// Check if this is a new top-level key
		sepIdx := -1
		if !isTOML {
			// YAML: look for first colon not in a string
			inQuote := false
			quoteChar := rune(0)
			for i, ch := range line {
				if !inQuote && (ch == '"' || ch == '\'') {
					inQuote = true
					quoteChar = ch
				} else if inQuote && ch == quoteChar {
					inQuote = false
				} else if !inQuote && ch == ':' {
					sepIdx = i
					break
				}
			}
		} else {
			// TOML: look for first =
			sepIdx = strings.Index(line, "=")
		}

		if sepIdx > 0 {
			potentialKey := strings.TrimSpace(line[:sepIdx])
			// Validate key: no spaces, not empty, first char is letter or underscore
			if potentialKey != "" && !strings.ContainsAny(potentialKey, " ") {
				// Save previous key if exists
				if currentKey != "" && inMultiline {
					// Preserve the multiline value as-is, just strip trailing whitespace
					multilineValue := strings.Join(currentValueLines, "\n")
					keyValues[currentKey] = strings.TrimRight(multilineValue, "\n")
				}

				currentKey = potentialKey
				keys = append(keys, currentKey)
				value := strings.TrimSpace(line[sepIdx+1:])

				// Strip comments from value
				value = stripComment(value)

				// Check if this starts a multiline value
				if value == "" || value == "null" || value == "~" || value == "true" || value == "false" {
					keyValues[currentKey] = value
					inMultiline = false
				} else if strings.HasSuffix(value, "|") || strings.HasSuffix(value, ">") ||
					(!isTOML && strings.HasSuffix(value, ":") && !strings.HasPrefix(value, "\"")) {
					inMultiline = true
					currentValueLines = nil
				} else if strings.HasPrefix(value, "[") && !strings.HasSuffix(value, "]") {
					// Multi-line array
					inMultiline = true
					currentValueLines = []string{value}
				} else {
					keyValues[currentKey] = value
					inMultiline = false
				}
				continue
			}
		}

		// If we're in multiline mode, collect lines with proper indentation
		if inMultiline && currentKey != "" {
			currentValueLines = append(currentValueLines, line)
		}
	}

	// Don't forget the last key
	if currentKey != "" && inMultiline {
		multilineValue := strings.Join(currentValueLines, "\n")
		keyValues[currentKey] = strings.TrimRight(multilineValue, "\n")
	}

	// Build output preserving all keys, with date value kept and others cleared
	var result []string
	result = append(result, "---")

	for _, key := range keys {
		if key == "date" {
			// Keep date value
			dateVal := keyValues[key]
			// Strip quotes if present
			dateVal = strings.Trim(dateVal, "\"'")
			if dateVal == "" || dateVal == "null" || dateVal == "~" {
				dateVal = time.Now().Format("2006-01-02T15:04:05+08:00")
			}
			result = append(result, fmt.Sprintf("%s: %s", key, dateVal))
		} else {
			// Clear other values
			result = append(result, fmt.Sprintf("%s: ", key))
		}
	}

	result = append(result, "---")
	result = append(result, "")

	return strings.Join(result, "\n")
}

func stripComment(value string) string {
	// Handle quoted strings - don't strip comments inside them
	inSingleQuote := false
	inDoubleQuote := false
	escaped := false

	for i, ch := range value {
		if escaped {
			escaped = false
			continue
		}
		if ch == '\\' {
			escaped = true
			continue
		}
		if !inDoubleQuote && ch == '"' {
			inDoubleQuote = !inDoubleQuote
			continue
		}
		if !inSingleQuote && ch == '\'' {
			inSingleQuote = !inSingleQuote
			continue
		}
		if !inSingleQuote && !inDoubleQuote {
			if ch == '#' {
				return strings.TrimSpace(value[:i])
			}
		}
	}
	return strings.TrimSpace(value)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
