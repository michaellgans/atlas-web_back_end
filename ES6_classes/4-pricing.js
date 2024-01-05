/* Task 4 */

import Currency from "./3-currency";

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw TypeError('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw TypeError('Currency must be an instance of Currency');
    }
    this._amount = amount;
    this._currency = currency;
  }
}
