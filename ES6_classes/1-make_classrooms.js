/* Task 1 */

import ClassRoom from './0-classroom.js';

const initializeRooms = () => {
  /* Stores values in a new array */
  const maxSize = [19, 20, 34];
  /* Creates new instances for each size in array! */
  return maxSize.map(size => new ClassRoom(size));
};

export default initializeRooms;
