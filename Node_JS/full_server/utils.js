// Task 8.1 - Accepts file path and reads DB
// (RUN ME FROM BASE OF FOLDER)

// Uses built in file system
const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    // Reads file from path asynchronously
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        // If can't find database, throw error
        reject(new Error('Cannot load the database'));
      } else {
        // Finding number of students
        const lines = data.trim().split('\n').slice(1);
        const records = lines.length;

        // Printed version for Task 5
        let result = `Number of students: ${records}\n`;

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

        // String version for Task 5
        Object.entries(nameByField).forEach(([field, listOfStudents]) => {
          result += `Number of students in ${field}: ${listOfStudents.length}. List: ${listOfStudents.join(', ')}\n`;
        });

        // Resolves promise
        resolve(result);
      }
    });
  });
}

module.exports = readDatabase;
