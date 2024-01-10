/* Task 10 */

export default function updateUniqueItems(oldMap) {

  if(!(oldMap instanceof Map)) {
    throw Error('Cannot process');
  }

  for (let [item, itemValue] of oldMap) {
    if (itemValue === 1) {
      oldMap.set(item, 100)
    }
  }
  return oldMap;
}
