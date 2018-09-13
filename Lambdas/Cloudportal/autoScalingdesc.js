'use strict';
var AWS = require('aws-sdk');
exports.handler = (event, context) => {
var number = (event.number === undefined ? 'No-Number' : event.number);
var region = (event.region === undefined ? 'us-east-1' : event.region);
var ASGroupName = (event.ASGroupName === undefined ? 'No-AutoScalingGroupNames' : event.ASGroupName);
var InstanceIds=[];
var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
    var autoscaling = new AWS.AutoScaling({apiVersion: '2011-01-01',region: region});
    console.log("test4");
} else {
var autoscaling = new AWS.AutoScaling({apiVersion: '2011-01-01',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
console.log("test2");
}



var params = {
  AutoScalingGroupNames: [
    ASGroupName,
    /* more items */
  ],
  //MaxRecords: 0,
  //NextToken: 'STRING_VALUE'
};
autoscaling.describeAutoScalingGroups(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else {
    //console.log(data);
    var agInstances =  data.AutoScalingGroups[0].Instances;           // successful response
    var InstanceIds = "";
 // console.log(data);
    //console.log(agInstances);
    for(var key in agInstances) {
      var InstanceId = agInstances[key].InstanceId;
      InstanceIds = InstanceId+","+InstanceIds;
    }
    InstanceIds = InstanceIds.substring(0,InstanceIds.length-1);
    console.log(InstanceIds);
    context.done(null, {InstanceIds});
  }
});
}
