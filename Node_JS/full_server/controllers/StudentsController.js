// Task 8.3 - Students Controller

import readDatabase from '../utils';

class StudentsController {
  // Controls information retrieved from database
  static async getAllStudents(req, res) {
    try {
      // Grabs the CSV file from user input
      const databasePath = process.argv[2];
      const result = await readDatabase(databasePath);

      // Sends Task 3 output
      res.type('type/plain');
      res.status(200).send(`This is the list of students\n${result}`);
    } catch (error) {
      // Catches Status 500
      console.log(error);
      res.status(500).send('Internal Server Error');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      // Grabs the CSV file from user input
      const databasePath = process.argv[2];
      const result = await readDatabase(databasePath);

      // If major passed to route is not CS or SWE
      const major = req.params.major;
      if (!['CS', 'SWE'].includes(major)) {
        res.status(400).send('Major parameter must be CS or SWE');
        return;
      }

      // Grabs students by major passed to the route
      const students = result
        .split('\n')
        .filter(line => line.includes('in ${major}'))
        .join('\n');
      
      res.type('type/plain');
      res.status(200).send(`List of students in ${major}:\n${students}`);
    } catch (error) {
      // Catches Status 500
      console.log(error);
      res.status(500).send('Internal Server Error');
    }
  }
}

module.exports = StudentsController;
