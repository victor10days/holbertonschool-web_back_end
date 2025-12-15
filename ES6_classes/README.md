# ES6 Classes

This project focuses on learning and implementing ES6 classes in JavaScript, including class definitions, methods, static methods, inheritance, and metaprogramming concepts.

## Project Details

- **Course**: [C#27] Foundations v2.1 - Part 3
- **Level**: Amateur
- **Author**: Johann Kerbrat, Engineering Manager at Uber Works
- **Weight**: 1

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external references:

- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Resources

- [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Metaprogramming](https://www.keithcirkel.co.uk/metaprogramming-in-es6-symbols/)

## Requirements

- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **node 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `.js` extension
- Code will be tested using **Jest**: `npm run test`
- Code will be verified against lint using **ESLint**
- Code needs to pass all tests and lint: `npm run full-test`

## Setup

### Install NodeJS 20.x.x

Run the following commands in your home directory:

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Verify installation:

```bash
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```

### Install Jest, Babel, and ESLint

In your project directory, install the required dependencies:

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### Configuration Files

You need the following configuration files in your project directory:

#### package.json

```json
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

#### babel.config.js

```javascript
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```

#### .eslintrc.js

```javascript
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
```

### Final Setup

After creating the configuration files, run:

```bash
npm install
```

## Usage

### Running Tests

To run all tests:

```bash
npm run test
```

### Linting

To check code style:

```bash
npm run check-lint
```

### Full Test (Lint + Tests)

To run both linting and tests:

```bash
npm run full-test
```

### Running Main Files

To execute main files with Babel:

```bash
npm run dev 0-main.js
```

## Project Structure

```
ES6_classes/
├── 0-classroom.js
├── 0-main.js
├── README.md
├── package.json
├── babel.config.js
└── .eslintrc.js
```

## Tasks

This project contains various tasks focused on implementing ES6 classes with different features and requirements. Each task file is numbered sequentially (e.g., `0-classroom.js`, `1-make_classrooms.js`, etc.).

## Author

**Victor Diaz** - Holberton School Student

---

**Project Duration**: Part of Holberton School's Foundations curriculum
