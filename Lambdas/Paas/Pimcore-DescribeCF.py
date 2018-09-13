import boto3
import time
import json


def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('cloudformation')
    ecsclient = boto3.client('ecs')
    print (event['StackName'])
    status = ""
    result = {}
    output = []
    try:
        response = client.describe_stacks(
            StackName=event['StackName']
        )
        status = response['Stacks'][0]['StackStatus']
        print (status)
        if 'Flag' in event and event['Flag'] == "DOCKER" and (status == "CREATE_COMPLETE" or status == "UPDATE_COMPLETE"):
            print ("Inside complete")
            tasklist = ecsclient.list_tasks(
                cluster=event['Cluster'],
                serviceName=event['ServiceName'],
                desiredStatus='RUNNING',
                launchType='EC2'
            )
            taskArns = tasklist['taskArns']
            tasksData = ecsclient.describe_tasks(
                cluster=event['Cluster'],
                tasks=taskArns
            )
            tasks = tasksData['tasks']
            containerInstances = []
            for task in tasks:
                containerInstances.append(task['containerInstanceArn'])
            containersInstancesData = ecsclient.describe_container_instances(
                cluster=event['Cluster'],
                containerInstances=containerInstances
            )
            containers = containersInstancesData['containerInstances']
            ec2InstanceIds = []
            for container in containers:
                ec2InstanceIds.append(container['ec2InstanceId'])
            ec2InstanceIdsStr = ",".join(list(set(ec2InstanceIds)))
            result['InstanceIds'] = ec2InstanceIdsStr
            
        if 'Outputs' in response['Stacks'][0]:
            output = response['Stacks'][0]['Outputs']
            
        result['HttpStatuscode'] = response['ResponseMetadata']['HTTPStatusCode']
        result['Status'] = status 
        result['StackName'] =  response['Stacks'][0]['StackName']
        result['Output'] = output
        result['Msg'] = 'Describe API initiated successfully'
        return result
    except Exception as e:
        print (e)
        result = { 'Msg': str(e) }
        return result
