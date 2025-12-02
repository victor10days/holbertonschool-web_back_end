# Python - Async

## Description

This project focuses on asynchronous programming in Python using the `asyncio` module. You'll learn how to write asynchronous coroutines, execute them concurrently, and understand the fundamentals of async/await syntax.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

- **async and await syntax**: Understanding how to define and call asynchronous functions
- **Execute an async program with asyncio**: Running asynchronous code using `asyncio.run()`
- **Run concurrent coroutines**: Executing multiple async operations simultaneously
- **Create asyncio tasks**: Using `asyncio.create_task()` to schedule coroutines
- **Use the random module**: Generating random values in asynchronous contexts

## Resources

### Read or watch:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

### Concepts:
- Python - Asynchronous execution
- Python - Asynchronous Programming

## Requirements

### General
- A `README.md` file at the root of the project folder is mandatory
- **Allowed editors**: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.9)
- All files should end with a new line
- All files must be executable
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should follow the **pycodestyle** style (version 2.5.x)
- All **functions and coroutines must be type-annotated**
- All **modules** should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
- All **functions** should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```
- Documentation should be meaningful sentences explaining the purpose, not just simple words

## Project Structure

```
holbertonschool-web_back_end/
└── python_async_function/
    ├── README.md
    ├── 0-basic_async_syntax.py
    └── [additional task files]
```

## Tasks

### 0. The basics of async (Mandatory)
Write an asynchronous coroutine that waits for a random delay and returns it.

**File**: `0-basic_async_syntax.py`

## Setup

### Make files executable:
```bash
chmod +x *.py
```

### Check code style:
```bash
pycodestyle *.py
```

### Test module documentation:
```bash
python3 -c 'print(__import__("0-basic_async_syntax").__doc__)'
```

### Test function documentation:
```bash
python3 -c 'print(__import__("0-basic_async_syntax").wait_random.__doc__)'
```

## Usage Example

```bash
./0-main.py
```

## Author

**Holberton School** - Python Async Function Project

## Repository

- **GitHub repository**: `holbertonschool-web_back_end`
- **Directory**: `python_async_function`
