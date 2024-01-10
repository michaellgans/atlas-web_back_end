/* Task 6 */

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo.reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const resultArray = [];

  try {
    const results = await Promise.allSettled([
      signUpUser(fileName, lastName),
      uploadPhoto(fileName),
    ]);

    results.forEach((result) => {
      resultArray.push({
        status: result.status,
        value: result.status === 'fulfilled' ? result.value : result.reason.toString(),
      });
    });
  } catch (error) {
    resultArray.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return resultArray;
}
