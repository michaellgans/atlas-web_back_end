/* Task 5 */

export default class Building {
  constructor(sqft) {
    if (!this.evacuationWarningMessage) {
        throw Error('Class extending Building must override evacuationWarningMessage')
    }
    if (typeof sqft !== 'number') {
        throw TypeError('Sqft must be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
