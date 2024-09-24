#!/usr/bin/node

import { createQueue } from 'kue';


const q = createQueue();

const data = {
  phoneNumber: '+201005489971',
  message: 'This is a job data',
}

const job = q
  .create('push_notification_code', data)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
