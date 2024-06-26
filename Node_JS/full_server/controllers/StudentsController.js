// Task 8.3 - Students Controller

import readDatabase from '../utils';

class StudentsController {
  // Controls information retrieved from database
  static getAllStudents(req, res) {
    try {
      // Grabs the CSV file from user input
      const readDatabase = process.argv[2];
  
      // Sends Task 3 output
      res.type('type/plain');
      res.status(200).send(`This is the list of students\n${result}`);
    } catch (error) {
      // Catches Status 500
      console.log(error);
      res.status(500).send('Internal Server Error');
    }
  }

  static getAllStudentsByMajor(req, res) {
    try {
      // Grabs the CSV file from user input
      const readDatabase = process.argv[2];
  
      // Sends Task 3 output
      res.type('type/plain');
      res.status(200).send(`This is the list of students\n${result}`);
    } catch (error) {
      // Catches Status 500
      console.log(error);
      res.status(500).send('Internal Server Error');
    }
  }
}

module.exports = StudentsController;
