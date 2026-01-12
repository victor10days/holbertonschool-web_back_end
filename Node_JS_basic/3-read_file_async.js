const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.trim().split('\n');

      const students = lines.slice(1).filter((line) => line.trim() !== '');
      let output = '';
      output += `Number of students: ${students.length}\n`;
      console.log(`Number of students: ${students.length}`);
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

      for (const [field, names] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
      resolve(output.trim());
    });
  });
}

module.exports = countStudents;
