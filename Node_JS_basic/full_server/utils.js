import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
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

    resolve(fields);
  });
});

export default readDatabase;
