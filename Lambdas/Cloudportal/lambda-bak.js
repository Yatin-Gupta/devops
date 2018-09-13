'use strict';
var AWS = require('aws-sdk');
console.log('Loading function');

exports.handler = (event, context) => {
        //console.log('Received event:', JSON.stringify(event, null, 2));
    //console.log('value1 =', event.key1);
    //console.log('value2 =', event.key2);
    //console.log('value3 =', event.key3);
   //callback(null, event.key1);  // Echo back the first key value
    //callback('Something went wrong');
    var number = (event.number === undefined ? 'No-Number' : event.number);
    var region = (event.region === undefined ? 'us-east-1' : event.region);
    var Instance_Id = (event.Instance_Id === undefined ? 'No-Instance-Id' : event.Instance_Id);
    var volIds = [];
    var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
    var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
    if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region});
    console.log("test1");
    } else {
    var ec2 = new AWS.EC2({apiVersion: '2016-04-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
    console.log("test2");
    }
    var params = {
  DryRun: false,
 
  InstanceIds:[
      Instance_Id,
      ],
  //MaxResults: 0
};
ec2.describeInstances(params, function(err, data) {
    console.log('"Hello2":"' + Instance_Id + '"');
  if (err) console.log(err, err.stack); // an error occurred
  //else console.log(data);
  else var data1 = data.Reservations[0].Instances[0].BlockDeviceMappings; //Successful response
  console.log(data1);
  for(var key in data1) {
      var volId = data1[key].Ebs.VolumeId;

      volIds = volIds + "," + volId;
      
      
};
      //alert("Key: " + key + " value: " + data1[key]);
    //}
  //var obj = JSON.parse(data);          
      
  //var data1 = data.Reservations
 
  //res.end(data["Reservations"]["ReservationId"].toString());
 
  context.done(null,{volIds});
 });

};
