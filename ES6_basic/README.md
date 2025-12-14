# ES6 Basic

This project covers the fundamentals of ECMAScript 6 (ES6), exploring modern JavaScript features and syntax.

## Description

This project contains exercises that demonstrate ES6 features including:
- `const` and `let` variable declarations
- Arrow functions
- Template literals
- Destructuring
- Spread/rest operators
- And other ES6 features

## Environment

- **Node.js**: v12.x or higher
- **npm**: v6.x or higher
- **Babel**: For ES6 transpilation
- **ESLint**: For code linting
- **Jest**: For testing

## Setup

1. Install dependencies:
```bash
npm install
```

2. The project uses:
   - Babel for transpiling ES6 code
   - ESLint for code quality checks
   - Jest for running tests

## Usage

Run JavaScript files using Babel:
```bash
npm run dev <filename>
```

Run tests:
```bash
npm test
```

Run linting:
```bash
npm run lint
```

## Example

```bash
npm run dev 0-main.js
# Output: I prefer const when I can. But sometimes let is okay
```

## Project Structure

- Configuration files:
  - [babel.config.js](babel.config.js) - Babel configuration
  - [.eslintrc.js](.eslintrc.js) - ESLint configuration
  - [package.json](package.json) - Project dependencies and Jest configuration

- Task files:
  - [0-constants.js](0-constants.js) - Working with `const` and `let`
  - [0-main.js](0-main.js) - Manual test file for task 0
  - [0-constants.test.js](0-constants.test.js) - Jest test file for task 0

## Tasks

### 0. Const or let?
File: [0-constants.js](0-constants.js)

Modify functions to use `const` and `let` appropriately:
- Use `const` when the variable is not reassigned
- Use `let` when the variable needs to be reassigned

## Author

Holberton School Project
