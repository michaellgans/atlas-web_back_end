// Task 11 - Tests 8-job.js

const { expect } = require('chai');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', function() {
  it('should test that jobs is an array', function(done) {
    expect(() => createPushNotificationsJobs({}, queue).to.throw(Error, 'Jobs is the wrong type'));
  });
});
