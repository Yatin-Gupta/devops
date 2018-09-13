'use strict';
var AWS = require('aws-sdk');
console.log('Loading function');
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var Instance_Id = (event.Instance_Id === undefined ? 'No-Instance Id' : event.Instance_Id);
var Description = (event.Description === undefined ? 'No-Description' : event.Description);
var ImageId = (event.ImageId === undefined ? 'No-ImageId' : event.ImageId);
var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
var SnapIds = [];
//if (Instance_Name === undefined || Instance_name === null ) {
//   return new Error("Instance_Name can not be empty of NULL");
//}
if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
    console.log("test1");
} else {
var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
console.log("test2");
};

var params = {
  ImageIds: [ImageId,], /* required */
  //Attribute: 'blockDeviceMapping', /* required */
  DryRun: false
};
ec2.describeImages(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else var data1 = data.Images[0].BlockDeviceMappings; //Successful response
  //console.log(data1);
    for(var key in data1) {
      var SnapId = data1[key].Ebs.SnapshotId;

      SnapIds = SnapIds + "," + SnapId;
      
      
};
  //for(var key in data1) {
//      var volId = data1[key].Ebs.VolumeId;

 //     volIds = volIds + "," + volId;
      
      
//};     
  //console.log(SnapIds);           // successful response
  context.done(null,{SnapIds});
});
}
