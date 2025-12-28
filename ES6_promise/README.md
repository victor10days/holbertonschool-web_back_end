# ES6 Promises

## Description

This project covers the fundamentals of JavaScript Promises and asynchronous programming in ES6. You'll learn how to handle asynchronous operations using Promises, async/await, and error handling with try/catch.

## Resources

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://web.dev/promises/)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)

## Learning Objectives

At the end of this project, you should be able to explain:

- **Promises**: how, why, and what they are
- How to use the `then`, `resolve`, and `catch` methods
- How to use every method of the Promise object
- `Throw` / `Try` error handling
- The `await` operator
- How to use an `async` function

## Requirements

- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **node 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a new line
- A `README.md` file at the root of the project is mandatory
- Code should use the `.js` extension
- Code will be tested using **Jest**: `npm run test`
- Code will be verified against lint using **ESLint**
- All functions must be exported

## Setup

### Install NodeJS 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Verify installation:

```bash
nodejs -v
# v20.15.1
npm -v
# 10.7.0
```

### Install Jest, Babel, and ESLint

In your project directory, run:

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint
```

### Configuration Files

Make sure you have the following configuration files in your project:

- `package.json`
- `babel.config.js`
- `.eslintrc.js`
- `utils.js` (for tasks requiring `uploadPhoto` and `createUser`)

**Don't forget to run:**

```bash
npm install
```

## Response Data Format

### uploadPhoto

Returns a response with the format:

```javascript
{
  status: 200,
  body: 'photo-profile-1',
}
```

### createUser

Returns a response with the format:

```javascript
{
  firstName: 'Guillaume',
  lastName: 'Salva',
}
```

## Project Structure

```
ES6_promise/
├── README.md
├── package.json
├── babel.config.js
├── .eslintrc.js
├── utils.js
└── [task files].js
```

## Testing

Run tests using:

```bash
npm run test
```

Run linter using:

```bash
npm run lint
```

## Author

**Holberton School** - Web Back-End Specialization

---

**Project Weight**: 1
**Level**: Amateur
**By**: Johann Kerbrat, Engineering Manager at Uber Works
