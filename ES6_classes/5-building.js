/* Task 5 */

export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
        throw TypeError('Sqft must be a number');
    };
  };
};
