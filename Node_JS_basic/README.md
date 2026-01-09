# Node.js Basics

This project covers fundamental concepts of Node.js, including file operations, HTTP servers, Express.js, and modern JavaScript with Babel.

## Learning Objectives

By completing this project, you will learn to:

- Run JavaScript using Node.js
- Use Node.js modules
- Use specific Node.js modules to read files
- Use process to access command line arguments and the environment
- Create a small HTTP server using Node.js
- Create a small HTTP server using Express.js
- Create advanced routes with Express.js
- Use ES6 with Node.js with Babel-node
- Use Nodemon to develop faster

## Requirements

- **Editors**: vi, vim, emacs, Visual Studio Code
- **Environment**: Ubuntu 20.04 LTS using Node.js (version 20.x.x)
- All files should end with a new line
- Code should use the `.js` extension
- Code will be tested using **Jest**: `npm run test`
- Code will be verified against lint using **ESLint**
- Code needs to pass all tests and lint: `npm run full-test`
- All functions/classes must be exported using: `module.exports = myFunction;`

## Project Structure

```
Node_JS_basic/
├── 0-console.js         # Basic console output
├── database.csv         # Sample student database
├── package.json         # Project dependencies and scripts
├── babel.config.js      # Babel configuration for ES6
├── .eslintrc.js         # ESLint configuration
└── README.md            # This file
```

## Setup

### Installation

Install all dependencies:

```bash
npm install
```

### Provided Files

#### database.csv
Sample CSV file containing student information:
- firstname
- lastname
- age
- field (CS or SWE)

#### package.json
Contains project scripts:
- `npm run lint` - Run ESLint on files
- `npm run check-lint` - Check lint on numbered files
- `npm run test` - Run tests with Mocha
- `npm run dev` - Run server in development mode with Nodemon
- `npm run full-test` - Run all tests and linting

#### babel.config.js
Configures Babel to transpile ES6+ code for Node.js

#### .eslintrc.js
ESLint configuration using Airbnb style guide with Jest plugin

## Usage

### Running Tests

Run all tests:
```bash
npm run test
```

Run tests and linting:
```bash
npm run full-test
```

### Linting

Check code style:
```bash
npm run check-lint
```

### Development Mode

Run the server with auto-reload:
```bash
npm run dev
```

## Technologies Used

- **Node.js** (v20.x.x) - JavaScript runtime
- **Express.js** (v4.17.1) - Web framework
- **Babel** - ES6+ transpiler
- **ESLint** - Code linting
- **Mocha** - Testing framework
- **Chai** - Assertion library
- **Nodemon** - Development auto-reload

## Resources

- [Node.js Getting Started](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Process API Documentation](https://nodejs.org/api/process.html)
- [Child Process](https://nodejs.org/api/child_process.html)
- [Express Getting Started](https://expressjs.com/en/starter/installing.html)
- [Mocha Documentation](https://mochajs.org/)
- [Nodemon Documentation](https://nodemon.io/)

## Author

Project by Johann Kerbrat, Engineering Manager at Uber Works

## License

ISC
