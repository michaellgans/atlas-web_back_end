// Task 8 - How to Create Jobs

const kue = require('kue');

// The Queue
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobs).save((err) => {
        if (!err) console.log('Notification job created:', job.id);
    });
    
    job.on('complete', () => {
        console.log('Notification job completed:', job.id);
    });
    
    job.on('failed', (err) => {
        console.log('Notification job failed:', job.id);
    });

    job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
