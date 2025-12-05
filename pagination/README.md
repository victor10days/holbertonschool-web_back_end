# Pagination

> Master the art of breaking down large datasets into manageable chunks

## 📚 Description

This project explores different pagination techniques used in REST APIs and backend systems. You'll learn how to implement simple pagination, hypermedia-driven pagination (HATEOAS), and deletion-resilient pagination strategies.

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- **How to paginate a dataset** with simple `page` and `page_size` parameters
- **How to paginate a dataset** with hypermedia metadata (HATEOAS)
- **How to paginate in a deletion-resilient manner** to handle data changes

## 🛠️ Resources

**Read or watch:**
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## 📋 Requirements

### General
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.9)**
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the **pycodestyle** style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your **functions and coroutines must be type-annotated**

### Documentation
- All modules must have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
- All functions must have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```
- Documentation must be **real sentences** explaining the purpose of the module, class, or method

## 📊 Setup: Data File

This project uses the **`Popular_Baby_Names.csv`** dataset for testing pagination implementations.

[Download the dataset here](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220228T205433Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=489c6e3be39e0e57b6e35f49c35e31d8eb6c8e1e65f2c25abc71e0e2e9f88588)

## 📁 Project Structure

```
pagination/
├── README.md
├── 0-simple_helper_function.py
├── 1-simple_pagination.py
├── 2-hypermedia_pagination.py
├── 3-hypermedia_del_pagination.py
└── Popular_Baby_Names.csv
```

## 🚀 Tasks

### 0. Simple helper function
Write a function `index_range` that returns a tuple of start and end indexes for pagination parameters.

### 1. Simple pagination
Implement a `Server` class that paginates a database of popular baby names.

### 2. Hypermedia pagination
Extend pagination with hypermedia metadata (HATEOAS principles).

### 3. Deletion-resilient hypermedia pagination
Implement pagination that remains consistent even when rows are deleted from the dataset.

## 💻 Usage Example

```python
#!/usr/bin/env python3
"""Example usage"""

index_range = __import__('0-simple_helper_function').index_range

# Get page 1 with 7 items per page
res = index_range(1, 7)
print(res)  # (0, 7)

# Get page 3 with 15 items per page
res = index_range(page=3, page_size=15)
print(res)  # (30, 45)
```

## 👤 Author

**Holberton School Project** - Web Back-end Specialization

## 📝 License

This project is part of the Holberton School curriculum.

---

*Happy Paginating! 📖✨*
