/* Task 2 */

export default class HolbertonCourse {
  constructor(name, length, students) {
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
      return;
    }
  }

  get length() {
    return this._length;
  }

  set length(x) {
    if (typeof x === 'number') {
      this._length = x;
    } else {
      return;
    }
  }

  get students() {
    return this._students;
  }

  set students(x) {
    if (Array.isArray(x)) {
      this._students = x;
    } else {
      return;
    }
  }
}
