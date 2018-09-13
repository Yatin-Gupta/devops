'use strict';
var AWS = require('aws-sdk');
let json = JSON.stringify(responseBody);
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var ASGroupName = (event.ASGroupName === undefined ? 'No-AutoScalingGroupNames' : event.ASGroupName);
var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
  let properties = null;

  try {
    properties = JSON.parse(process.argv[2]);
  } catch (error) {
    console.error('Invalid JSON: ', error);
    
}
var InstanceIds=[];

if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
    console.log("test1");
} else {
var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
console.log("test2");
}

  if (typeof properties.Name === 'undefined') {
    return callback(new Error('The Name property was not specified.'));
  }

  let owners = ['self'];
  if (typeof properties.Owners !== 'undefined') {
    if (!Array.isArray(properties.Owners)) {
      return callback(new Error('The Owners property must be an array.'));
    }
    owners = properties.Owners;
