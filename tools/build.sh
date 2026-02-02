#!/bin/bash

# cr build script

BINARY_NAME="cr"
MAIN_FILE="main.go"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_error() {
    echo -e "${RED}Error: $1${NC}"
}

print_success() {
    echo -e "${GREEN}$1${NC}"
}

print_info() {
    echo -e "${YELLOW}$1${NC}"
}

# Function to build the binary
build() {
    print_info "Building ${BINARY_NAME}..."
    if go build -o "${BINARY_NAME}" "${MAIN_FILE}"; then
        print_success "Build complete: ${BINARY_NAME}"
    else
        print_error "Build failed"
        exit 1
    fi
}

# Function to clean build artifacts
clean() {
    print_info "Cleaning..."
    if [ -f "${BINARY_NAME}" ]; then
        rm "${BINARY_NAME}"
        print_success "Clean complete"
    else
        print_info "Nothing to clean"
    fi
}

# Function to install the binary
install() {
    build
    print_info "Installing ${BINARY_NAME} to /usr/local/bin..."
    if sudo cp "${BINARY_NAME}" /usr/local/bin/; then
        print_success "Install complete"
    else
        print_error "Install failed"
        exit 1
    fi
}

# Function to test the binary
test() {
    build
    print_info "Testing ${BINARY_NAME}..."
    if ./"${BINARY_NAME}" --help > /dev/null 2>&1; then
        print_success "Test passed"
    else
        print_error "Test failed"
        exit 1
    fi
}

# Function to show help
show_help() {
    echo "Usage: $0 {build|clean|install|test|help}"
    echo ""
    echo "Commands:"
    echo "  build   - Build the binary"
    echo "  clean   - Remove the binary"
    echo "  install - Build and install to /usr/local/bin (requires sudo)"
    echo "  test    - Build and test the binary"
    echo "  help    - Show this help message"
}

# Main script logic
case "${1:-build}" in
    build)
        build
        ;;
    clean)
        clean
        ;;
    install)
        install
        ;;
    test)
        test
        ;;
    help)
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac
