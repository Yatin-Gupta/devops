
'use strict';
var AWS = require('aws-sdk');
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var Instance_Id = (event.Instance_Id === undefined ? 'No-Instance_Id' : event.Instance_Id);
var Snap_Id = (event.Snap_Id === undefined ? 'No-Snap_Id' : event.Snap_Id);
var tag_Name = (event.tag_Name === undefined ? 'No-tag_Name' : event.tag_Name);

var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var rds = new AWS.RDS({apiVersion: '2014-10-31',region: region});
} else {
var rds = new AWS.RDS({apiVersion: '2014-10-31',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
}
var params = {
  DBInstanceIdentifier: Instance_Id, /* required */
  DBSnapshotIdentifier: Snap_Id, /* required */
  Tags: [
    {
      Key: 'Backup',
      Value: tag_Name
    },
    /* more items */
  ]
};
rds.createDBSnapshot(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     context.done(null,{data});           // successful response
});
}   
