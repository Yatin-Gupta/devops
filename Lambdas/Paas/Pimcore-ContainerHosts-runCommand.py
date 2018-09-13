import boto3
import time
import datetime

def lambda_handler(event, context):
    
    ssmclient = boto3.client('ssm')
    ssmRunInstances = [ event['InstanceId'] ] # will get from database
    for instance in ssmRunInstances:
        response = ssmclient.send_command(
            InstanceIds=[instance],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': [
                     'mkdir -p /opt/' + event['CompanyName'] + '_' + str(int(time.time()))
                ]
            }
        )
    commands = response["Command"]["Parameters"]["commands"]
    instanceids = response["Command"]["InstanceIds"]
    directories = []
    findStr = "mkdir -p "
    
    for command in commands:
        temp = command
        mkdirPos = temp.find(findStr)
        if mkdirPos >= 0:
            directories.append(temp[(mkdirPos+len(findStr)):])
    result = { 'InstanceIds': instanceids, 'Directories': directories }
    print (result)
    return result