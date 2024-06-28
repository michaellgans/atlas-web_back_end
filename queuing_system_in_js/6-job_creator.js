// Task 6 - Create the Job Creator

const kue = require('kue');

// The Queue
const push_notification_code = kue.createQueue();

// The Job
const jobObject = {
    phoneNumber: '867-5309',
    message: 'Jenny\'s Number',
};

const job = push_notification_code.create('push_notification', jobObject).save((err) => {
    if (!err) console.log('Notification job created:', job.id);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', (err) => {
    console.log('Notification job failed');
});