"use strict";
var AWS = require('aws-sdk');
exports.handler = (event, context, callback) => {
    // TODO implement
    var number = (event.number === undefined ? 'No-Number' : event.number);
    var region = (event.region === undefined ? 'us-east-1' : event.region);
    var Snap_Id = (event.Snap_Id === undefined ? 'No-Snap_Id' : event.Snap_Id);
    var accessKey = (event.accessKey === undefined ? 'No-accesskey' : event.accessKey);
    var secretKey = (event.secretKey === undefined ? 'No-secretkey' : event.secretKey);
    if (accessKey === "No-accesskey" || accessKey === null || secretKey === "No-secretkey" || secretKey ===null) {
        var rds = new AWS.RDS({apiVersion: '2014-10-31',region: region});
    } else {
        var rds = new AWS.RDS({apiVersion: '2014-10-31',region: region, accessKeyId: accessKey, secretAccessKey: secretKey});
    }
    
    var params = {
        DBSnapshotIdentifier: Snap_Id
    };
    rds.deleteDBSnapshot(params, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else {     
            console.log(data);           // successful response
            callback(null, "Snapshot deleted successfully");
        }
});
    
};
