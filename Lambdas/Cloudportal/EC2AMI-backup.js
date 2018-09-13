'use strict';
var AWS = require('aws-sdk');

console.log('Loading function');
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var Instance_Id = (event.Instance_Id === undefined ? 'No-Instance Id' : event.Instance_Id);
var Description = (event.Description === undefined ? 'No-Description' : event.Description);
var Instance_Name = (event.Instance_Name === undefined ? 'No-Instance name' : event.Instance_Name);
var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
//if (Instance_Name === undefined || Instance_name === null ) {
//   return new Error("Instance_Name can not be empty of NULL");
//}
if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
    console.log("test1");
} else {
var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
console.log("test2");
}
var params = {
  InstanceId: Instance_Id, /* required */
  Name: Instance_Name, /* required */
  Description: Description,
  DryRun: false,
  NoReboot: true
};
ec2.createImage(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else {     
     // successful response
     console.log("Image created successful");
     console.log(data);
  }
  context.done(null,{data});
});
}
