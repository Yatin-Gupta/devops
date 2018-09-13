import boto3
import time
import datetime
import json

def lambda_handler(event, context):

    ec2client = boto3.client('ec2')
    project = event['Project']

    
    instance = event['instanceId']
    
    ssmclient = boto3.client('ssm')
    response = ssmclient.send_command(
        InstanceIds=[instance],
        DocumentName='AWS-RunShellScript',
        TimeoutSeconds=300,
        Parameters={
            'commands': [
                '/opt/Pimcore_script1.sh ' + project #+ '&& rm -f /opt/Pimcore_script1.sh'
            ]
        }
    )
    
    commandId = response['Command']['CommandId']
    print ("CommandID is " +  commandId)
    loop = True
    time.sleep(30)
    while loop:
        time.sleep(30)
        response1 = ssmclient.list_command_invocations(
            CommandId=commandId,
            InstanceId=instance,
            Details=True
        )
        if not response1['CommandInvocations']:
            print("response1 is not present")
            loop = True
        else:
            status = response1['CommandInvocations'][0]['Status']
            print("Status is yet not ready")
            if status != 'Pending' and status != 'InProgress':
                print("Status is ready")
                loop = False
    
    status = response1['CommandInvocations'][0]['CommandPlugins'][0]['Status']
    output = response1['CommandInvocations'][0]['CommandPlugins'][0]['Output']
    outputAr = output.split("\n")
    presignURLStr = outputAr[2]
    findStr = "Output: Presign URL: "
    presignURL = presignURLStr[len(findStr):]
    result = { 'InstanceId': instance, 'Project': project, 'CommandId': commandId, 'Status': status, 'PresignURL': presignURL, 'Output': output }
    print (result)
    return json.dumps(result)