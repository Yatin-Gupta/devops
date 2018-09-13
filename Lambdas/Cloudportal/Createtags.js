'use strict';
var AWS = require('aws-sdk');
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var resource_Id = (event.resource_Id === undefined ? 'No-resourceId' : event.resource_Id);
var tag_Name = (event.tag_Name === undefined ? 'No-tag_Name' : event.tag_Name);
var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
    console.log("test1");
} else {
var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
console.log("test2");
}
var paramstag = {
      Resources: [
     resource_Id
  ],
  Tags: [
     {
    Key: "Name",
    Value: tag_Name
   }
  ]
};
 ec2.createTags(paramstag, function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);           // successful response
   
 });
}
