const http = require('http');
const fs = require('fs');

const database = process.argv[2];

function buildStudentsReport(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }
            const lines = data.trim().split('\n');
            const students = lines.slice(1).filter((line) => line.trim() !== '');
            const fields = {};

            for (const line of students) {
                const parts = line.split(',');
                const firstname = parts[0].trim();
                const field = parts[3].trim();
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstname);
            }

            const output = [];
            output.push(`Number of students: ${students.length}`);
            for (const [field, names] of Object.entries(fields)) {
                output.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }

            resolve(output.join('\n'));
        });
    });
}

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  
  if (req.url === '/') {
    res.end('Hello Holberton School!');
    return;
  }
    if (req.url === '/students') {
        const header = 'This is the list of our students\n';
        buildStudentsReport(database)
        .then((report) => {
            res.end(header + report);
        })
        .catch((err) => {
            res.end(err.message);
        });
    } else {
        res.end('Hello Holberton School!');
    }
});

app.listen(1245, () => {});
module.exports = app;
