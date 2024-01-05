/* Task 2 */

export default class HolbertonCourse {
  constructor(name, length, students) {
    /* Guard for types */
    if (typeof name !== 'string') {
        throw TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
        throw TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
        throw TypeError('Students must be an array of strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  /* Getter and Setter for name */
  get name() {
    return this._name;
  }

  set name(x) {
    if (typeof x !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      return this._name;
    }
  }

  /* Getter and setter for length */
  get length() {
    return this._length;
  }

  set length(x) {
    if (typeof x === 'number') {
      throw TypeError('Length must be a number');
    } else {
      return this._length;
    }
  }

  /* Getter and Setter for students */
  get students() {
    return this._students;
  }

  set students(x) {
    if (!Array.isArray(x)) {
      throw TypeError('Students must be an array of strings');
    } else {
      return this._students;
    }
  }
}
