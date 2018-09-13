'use strict';
var AWS = require('aws-sdk');
console.log('Loading function');
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var volume_Id = (event.volume_Id === undefined ? 'No-volume Id' : event.volume_Id);
var Description = (event.Description === undefined ? 'No-Description' : event.Description);
var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
var snapId = [];
//if (Instance_Name === undefined || Instance_name === null ) {
//   return new Error("Instance_Name can not be empty of NULL
//}
//var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
    console.log("test1");
} else {
var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
console.log("test2");
}

var params = {
  VolumeId: volume_Id, /* required */
  Description: Description,
  DryRun: false
};

ec2.createSnapshot(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
  snapId=data.SnapshotId.toString();
  console.log(snapId);
  context.done(null,{data});
});



};
