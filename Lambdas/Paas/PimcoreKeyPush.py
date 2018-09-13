
from __future__ import print_function

import json
import urllib.parse
import boto3

print('Loading function')

def lambda_handler(event, context):
    AWS_BUCKET_NAME='pimcorekeybucket'
    privatekey = event['key']
    instance = event['instance']
    s3FileBody = ""
    
    for line in privatekey:
        s3FileBody += line + "\n"
    s3FileBody = s3FileBody[:-1]
    print(s3FileBody)
    client = boto3.client('s3')
    response = {}
    statusCode = 0
    pre_url = ""
    try:
        response = client.put_object(
            ACL='private',
            Body=s3FileBody,
            Bucket=AWS_BUCKET_NAME,
            ContentEncoding='utf-8',
            Key=instance + "/" + instance + '.pk',
            StorageClass='STANDARD'
        )
        print (response)
        statusCode = int(response['ResponseMetadata']['HTTPStatusCode'])
        if statusCode == 200:
            pre_url = client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': AWS_BUCKET_NAME,
                    'Key': instance + "/" + instance + '.pk'
                }
            )
        response = { "pre_url": pre_url, "errmsg": "", "statusCode": statusCode }
    except Exception as e:
        print(e)
        response = { "pre_url": pre_url, "errmsg": str(e), "statusCode": statusCode }
        print('Error puttin object {} to bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(instance, AWS_BUCKET_NAME))
        raise e
    finally:
        return response