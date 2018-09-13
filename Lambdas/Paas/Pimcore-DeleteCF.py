import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('cloudformation')
    #event = event["body-json"]
    result = {}
    try:
        response = client.delete_stack(
            StackName=event["StackName"]
        )
        result['HttpStatusCode'] = response['ResponseMetadata']['HTTPStatusCode']
        result['Msg'] = 'Stack Deletion initiated successfully'
        result['StackName'] = event["StackName"]
        print (result)
        return result
    except Exception as e:
        result['Msg'] = str(e)
        print (str(e))
        return result