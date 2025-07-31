# Python - Async Function

This project explores asynchronous programming in Python using the `asyncio` module. It demonstrates the concepts of async/await syntax, concurrent coroutines, asyncio tasks, and timing measurements.

## Learning Objectives

- Understanding async and await syntax
- Executing async programs with asyncio
- Running concurrent coroutines
- Creating asyncio tasks
- Using the random module with async functions

## Project Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- All files must be executable
- Code should use the pycodestyle style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules and functions should have proper documentation

## Files

### 0-basic_async_syntax.py
Contains the `wait_random` coroutine that waits for a random delay between 0 and max_delay seconds.

**Usage:**
```python
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

### 1-concurrent_coroutines.py
Contains the `wait_n` async routine that spawns `wait_random` n times with specified max_delay and returns delays in ascending order without using `sort()`.

**Usage:**
```python
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
```

### 2-measure_runtime.py
Contains the `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine.

**Usage:**
```python
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9
print(measure_time(n, max_delay))
```

### 3-tasks.py
Contains the `task_wait_random` function that creates and returns an asyncio Task for the `wait_random` coroutine.

**Usage:**
```python
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4-tasks.py
Contains the `task_wait_n` function that uses `task_wait_random` to create n tasks and returns delays in ascending order.

**Usage:**
```python
import asyncio
task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

## Key Concepts Demonstrated

1. **Asynchronous Coroutines**: Functions defined with `async def` that can be paused and resumed
2. **Concurrent Execution**: Running multiple coroutines simultaneously using `asyncio.as_completed()`
3. **Task Creation**: Converting coroutines to tasks using `asyncio.create_task()`
4. **Random Delays**: Using `random.uniform()` to generate random floating-point delays
5. **Time Measurement**: Using the `time` module to measure execution time
6. **Natural Sorting**: Maintaining order without using `sort()` by inserting elements in correct positions

## Author

Project completed as part of the Holberton School Web Back End curriculum.