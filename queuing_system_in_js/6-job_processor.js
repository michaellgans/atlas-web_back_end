// Task 6 - Create the Job Processor

const kue = require('kue');

// The Queue
const queue = kue.createQueue();

// Job Processor
queue.process('push_notification', (job, done) => {
    const { phoneNumber, message } = job.data;

    // Sends notification to phone number
    sendNotification(phoneNumber, message);
    // Tells Kue the job is complete
    done();
});

// Creates notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}


