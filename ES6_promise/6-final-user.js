/* Task 6 */

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject.js';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const resultArray = [];

  await Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ])
  .then (async (result) => {
      resultArray.push({
        status: result.status,
        value: result.value,
      });
  })
  .catch ((error) => {
    resultArray.push({
      status: 'rejected',
      value: error.toString(),
    });
  });
}
