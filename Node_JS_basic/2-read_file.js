const fs = require('fs');

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  const lines = data.trim().split('\n');

  const students = lines.slice(1).filter((line) => line.trim() !== '');
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
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
