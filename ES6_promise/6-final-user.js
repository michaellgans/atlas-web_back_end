/* Task 6 */

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const resultArray = [];

  try {
    const userResult = await signUpUser(fileName, lastName);
      resultArray.push({
        status: 'fulfilled',
        value: { firstName, lastName },
      });

    const photoResult = await uploadPhoto(fileName);
    resultArray.push({
      status: 'fulfilled',
      value: photoResult,
    });
  } catch (error) {
    resultArray.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return resultArray;
}
