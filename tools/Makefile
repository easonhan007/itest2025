# cr Makefile
BINARY_NAME=cr
MAIN_FILE=main.go
BUILD_DIR=.

# Default target
.PHONY: all build clean install help

all: build

build:
	@echo "Building $(BINARY_NAME)..."
	go build -o $(BUILD_DIR)/$(BINARY_NAME) $(MAIN_FILE)
	@echo "Build complete: $(BUILD_DIR)/$(BINARY_NAME)"

clean:
	@echo "Cleaning..."
	rm -f $(BUILD_DIR)/$(BINARY_NAME)
	@echo "Clean complete"

install: build
	@echo "Installing $(BINARY_NAME) to /usr/local/bin..."
	cp $(BUILD_DIR)/$(BINARY_NAME) /usr/local/bin/
	@echo "Install complete"

test: build
	@echo "Running tests..."
	./$(BINARY_NAME) --help

help:
	@echo "Available targets:"
	@echo "  make build    - Build the binary"
	@echo "  make clean    - Remove the binary"
	@echo "  make install  - Build and install to /usr/local/bin"
	@echo "  make test     - Build and run help test"
	@echo "  make help     - Show this help message"
