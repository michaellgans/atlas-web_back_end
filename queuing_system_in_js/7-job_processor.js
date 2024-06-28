// Task 7 - Create the Job Processor

const kue = require('kue');

// The Queue
const queue = kue.createQueue();

// Blacklisted Phonenumbers
const blackListed = ['4153518780', '4153518781'];

// Creates notification
function sendNotification(phoneNumber, message, job, done) {
    // 0% progress
    job.progress(0, 100);

    // Reject blacklist
    if (blackListed.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // 50% progress
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Tell Kue job is completed
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
