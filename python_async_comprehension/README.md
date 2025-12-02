# Python - Async Comprehension

## Description

This project explores advanced asynchronous programming concepts in Python, focusing on asynchronous generators and comprehensions. You'll learn how to write async generators, use async comprehensions, and properly type-annotate generator functions.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

- **Write an asynchronous generator**: Create generators that can use `await` and yield values asynchronously
- **Use async comprehensions**: Leverage Python's async list/dict/set comprehensions
- **Type-annotate generators**: Properly add type hints to generator functions using `typing` module

## Resources

### Read or watch:
- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What's New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

### Concepts:
- Python - Asynchronous execution
- Python - Asynchronous Programming

## Requirements

### General
- **Allowed editors**: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow the **pycodestyle** style (version 2.5.x)
- All files must be executable
- All **modules** should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
- All **functions and coroutines** should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```
- Documentation should be meaningful sentences explaining the purpose, not just simple words
- All **functions and coroutines must be type-annotated**

## Project Structure

```
holbertonschool-web_back_end/
└── python_async_comprehension/
    ├── README.md
    ├── 0-async_generator.py
    └── [additional task files]
```

## Tasks

### 0. Async Generator (Mandatory)
Write a coroutine that yields random numbers asynchronously.

**File**: `0-async_generator.py`

## Key Concepts

### Asynchronous Generators
- Combine `async def` with `yield` statements
- Can use `await` inside the generator
- Consumed using `async for` loops

### Async Comprehensions
- List comprehensions: `[x async for x in async_generator()]`
- Dict comprehensions: `{x: x async for x in async_generator()}`
- Set comprehensions: `{x async for x in async_generator()}`

### Type Annotations for Generators
```python
from typing import AsyncGenerator

async def my_generator() -> AsyncGenerator[int, None]:
    yield 1
```

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
python3 -c 'print(__import__("0-async_generator").__doc__)'
```

### Test function documentation:
```bash
python3 -c 'print(__import__("0-async_generator").async_generator.__doc__)'
```

## Usage Example

```bash
./0-main.py
```

## Author

**Holberton School** - Python Async Comprehension Project

## Repository

- **GitHub repository**: `holbertonschool-web_back_end`
- **Directory**: `python_async_comprehension`
