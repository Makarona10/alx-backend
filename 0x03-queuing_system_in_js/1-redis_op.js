#!/usr/bin/node

import redis from 'redis';


const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (_, value) => {
    console.log(value);
  });
};
