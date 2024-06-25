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
        console.log(`I found this: \n${data}`);
    });
}

//     // If database found, display Number of Students
//     const num_of_students = 
//     const field = 
//     const students_in_field = 
//     const list_in_field = 

//     console.log(`Number of students: ${num_of_students}`)
//     console.log(`Number of students in ${field}: ${students_in_field}`);
//   }
  
  module.exports = countStudents;
