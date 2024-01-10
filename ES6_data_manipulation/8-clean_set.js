/* Task 8 */

export default function cleanSet(set, startString) {
  let result = '';

  if (startString.length < 1) {
    return '';
  }

  if (!startString) {
    return '';
  }

  for (const item of set) {
    if (item.startsWith(startString)) {
      result += item.substring(startString.length) + '-';
    }
  }

  return result.slice(0, -1);
}
