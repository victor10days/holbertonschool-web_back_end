const express = require('express');

const countStudents = require('./3-read_file_async');

const app = express();

const database = process.argv[2];

app.get('/', (req, res) => {
    res.status(200).send('Hello Holberton School!');
    }
);

app.get('/students', async (req, res) => {
    let responseText = 'This is the list of our students\n';
    try {
        const report = await countStudents(database);
        responseText += report;
        res.status(200).send(responseText);
    } catch (err) {
        responseText += err.message;
        res.status(200).send(responseText);
    }
});

app.listen(1245, () => {});

module.exports = app;
