/* Task 6 */

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo.reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(), uploadPhoto()])
    .then ({
        status: promiseStatus,
        value: value,
    })
    .catch (new Error())
}
