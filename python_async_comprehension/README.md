# Python - Async Comprehension

This project demonstrates the implementation of asynchronous generators, async comprehensions, and parallel execution in Python. It covers advanced async/await patterns and performance measurement techniques.

## Learning Objectives

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators
- How to measure runtime of parallel async operations

## Requirements

- Python 3.9+
- Ubuntu 20.04 LTS
- Code style: pycodestyle (version 2.5.x)
- All functions and coroutines must be type-annotated

## Files

### 0-async_generator.py
**Async Generator Implementation**

Contains an asynchronous generator that:
- Loops 10 times
- Waits 1 second asynchronously on each iteration
- Yields a random float between 0 and 10

```python
async def async_generator() -> Generator[float, None, None]:
    """Async generator that yields 10 random numbers with 1-second delays."""
```

**Usage Example:**
```python
import asyncio
from 0-async_generator import async_generator

async def main():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(main())
```

### 1-async_comprehension.py
**Async Comprehension Implementation**

Uses async comprehension syntax to collect 10 random numbers from the async generator:

```python
async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension."""
```

**Usage Example:**
```python
import asyncio
from 1-async_comprehension import async_comprehension

async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())
```

### 2-measure_runtime.py
**Parallel Execution and Runtime Measurement**

Executes 4 async comprehensions in parallel using `asyncio.gather()` and measures total runtime:

```python
async def measure_runtime() -> float:
    """Execute 4 async comprehensions in parallel and measure runtime."""
```

**Usage Example:**
```python
import asyncio
from 2-measure_runtime import measure_runtime

async def main():
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime} seconds")

asyncio.run(main())
```

## Key Concepts Demonstrated

### 1. Asynchronous Generators
- Use `async def` with `yield` to create async generators
- Allow asynchronous iteration with `async for`
- Enable non-blocking iteration over async data sources

### 2. Async Comprehensions
- Syntax: `[expr async for item in async_iterable]`
- Provide concise way to collect results from async generators
- Introduced in Python 3.6 (PEP 530)

### 3. Parallel Execution
- `asyncio.gather()` runs multiple coroutines concurrently
- Significantly improves performance for I/O-bound operations
- Runtime is ~10 seconds (not 40 seconds) because operations run in parallel

### 4. Type Annotations
- Generators: `Generator[YieldType, SendType, ReturnType]`
- Async functions: `async def func() -> ReturnType:`
- Lists: `List[ElementType]`

## Performance Analysis

The `measure_runtime()` function demonstrates the power of async programming:

- **Sequential execution** would take: 4 × 10 seconds = 40 seconds
- **Parallel execution** takes: ~10 seconds (the time of the longest operation)

This 4x performance improvement occurs because:
1. Each async comprehension takes ~10 seconds (10 iterations × 1 second each)
2. `asyncio.gather()` runs all 4 comprehensions concurrently
3. Total time equals the duration of the longest operation, not the sum

## Testing

To test the implementations:

```bash
# Test async generator
python3 -c "
import asyncio
from 0-async_generator import async_generator

async def test():
    result = []
    async for i in async_generator():
        result.append(i)
    print(f'Generated {len(result)} numbers')

asyncio.run(test())
"

# Test async comprehension
python3 -c "
import asyncio
from 1-async_comprehension import async_comprehension

async def test():
    result = await async_comprehension()
    print(f'Collected {len(result)} numbers: {result}')

asyncio.run(test())
"

# Test runtime measurement
python3 -c "
import asyncio
from 2-measure_runtime import measure_runtime

async def test():
    runtime = await measure_runtime()
    print(f'Runtime: {runtime:.2f} seconds')

asyncio.run(test())
"
```

## Code Style

All code follows PEP 8 guidelines and passes pycodestyle checks:

```bash
pycodestyle *.py
```

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [Type hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

---

**Author:** Holberton School Web Backend Curriculum  
**Project:** Python - Async Comprehension