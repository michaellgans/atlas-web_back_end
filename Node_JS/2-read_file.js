// Task 2 - Read csv file

// Uses built in file system
const fs = require('fs');

function countStudents(path) {
  // Reads file from path synchronously
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      // If can't find database, throw error
      console.log('Cannot load the database');
      return;
    }

    // Finding number of students
    const lines = data.trim().split('\n').slice(1);
    const records = lines.length;

    console.log(`Number of students: ${records}`);

    // Pulling first name and field into an object
    const nameByField = {};

    lines.forEach((line) => {
      const [firstname, , , field] = line.split(',');

      // Sorts first names into arrays by field
      if (!nameByField[field]) {
        nameByField[field] = [];
      }
      nameByField[field].push(firstname);
    });

    // Prints number of students by field and lists the students
    Object.entries(nameByField).forEach(([field, listOfStudents]) => {
      console.log(`Number of students in ${field}: ${listOfStudents.length}. List: ${listOfStudents.join(', ')}`);
    });
  });
}

module.exports = countStudents;
