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

  get name() {
    return this._name;
  }

  set name(x) {
    if (typeof x === 'string') {
      this._name = x;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(x) {
    if (typeof x === 'number') {
      this._length = x;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(x) {
    if (Array.isArray(x)) {
      this._students = x;
    } else {
      throw TypeError('Students must be an array of strings');
    }
  }
}
