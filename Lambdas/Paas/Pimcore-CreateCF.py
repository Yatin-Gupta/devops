import boto3
import json
import urllib
import uuid
import re


def lambda_handler(event, context):
    client = boto3.client('cloudformation')
    ecsclient = boto3.client('ecs')
    Stage = event['Stage']
    StackName = ""
    stackParams = []
    result = {}
    resourceTypes = []
    if 'Flag' in event:
        if event['Flag'] == "DOCKER":
            resourceTypes = [
                'AWS::ECS::Service',
                'AWS::ECS::TaskDefinition',
                'AWS::Logs::LogGroup',
                'AWS::ElasticLoadBalancingV2::TargetGroup',
                'AWS::ElasticLoadBalancingV2::ListenerRule'
            ]
        elif event['Flag'] == "INSTANCE":
            if Stage == "POC":
                resourceTypes = [
                    "AWS::EC2::Instance",
                    "AWS::EC2::SecurityGroup",
                    "AWS::IAM::Role",
                    "AWS::ElasticLoadBalancingV2::TargetGroup",
                    "AWS::ElasticLoadBalancingV2::ListenerRule",
                    "AWS::IAM::InstanceProfile"
                ]
            elif Stage == "Demo7":
                resourceTypes = [
                    "AWS::EC2::Instance"
                ]
        elif event['Flag'] == "LOADBALANCER":
            if Stage == "POC":
                resourceTypes = [
                    "AWS::ElasticLoadBalancingV2::LoadBalancer",
                    "AWS::ElasticLoadBalancingV2::Listener",
                    "AWS::ElasticLoadBalancingV2::TargetGroup",
                    "AWS::EC2::SecurityGroup"
                ]
    if Stage == 'POC':
        if 'Flag' in event:
            if event['Flag'] == "LOADBALANCER":
                TemplateURL= 'https://s3.amazonaws.com/pimcoreservicetasktemplates/POC/POC-load-balancer_v1.yml'
                StackName = 'PimcorePOC-' + str(event['ALBPrefix'])
                stackParams = [
                    {
                        'ParameterKey': 'Stage',
                        'ParameterValue': event['Stage']
                    },
                    {
                        'ParameterKey': 'ALBPrefix',
                        'ParameterValue': event['ALBPrefix']
                    },
                    {
                        'ParameterKey': 'VPC',
                        'ParameterValue': event['VPC']
                    },
                    {
                        'ParameterKey': 'Subnets',
                        'ParameterValue': event['Subnets']
                    },
                    {
                        'ParameterKey': 'LoadBalancerCertificateArn',
                        'ParameterValue': event['LoadBalancerCertificateArn']
                    }
                    
                ]
            elif event['Flag'] == "INSTANCE":
                TemplateURL = "https://s3.amazonaws.com/pimcoreservicetasktemplates/POC/POC_v2.yml"
                StackName = 'PimcorePOCInstance' + str(event['Priority'])
                result['HostPattern'] = 'pgspoc' + str(event['Priority']) + '.pimcoreclients.com'
                stackParams = [
                    {
                        'ParameterKey': 'Priority',
                        'ParameterValue': str(event['Priority'])
                    },
                    {
                        'ParameterKey': 'HostPattern',
                        'ParameterValue': 'pgspoc' + str(event['Priority']) + '.pimcoreclients.com'
                    },
                    {
                        'ParameterKey': 'PROJECT',
                        'ParameterValue': event['PROJECT']
                    },
                    {
                        'ParameterKey': 'CompanyName',
                        'ParameterValue': event['CompanyName']
                    },
                    {
                        'ParameterKey': 'InstanceType',
                        'ParameterValue': event['InstanceType']
                    },
                    {
                        'ParameterKey': 'SSHClientIP1',
                        'ParameterValue': event['SSHClientIP1']
                    },
                    {
                        'ParameterKey': 'SSHClientIP2',
                        'ParameterValue': event['SSHClientIP2']
                    },
                    {
                        'ParameterKey': 'KeyFile',
                        'ParameterValue': event['KeyFile']
                    },
                    {
                        'ParameterKey': 'LoadBalancerSecurityGroup',
                        'ParameterValue': event['LoadBalancerSecurityGroup']
                    },
                    {
                        'ParameterKey': 'Listener',
                        'ParameterValue': event['Listener']
                    },
                    {
                        'ParameterKey': 'Stage',
                        'ParameterValue': event['Stage']
                    },
                    {
                        'ParameterKey': 'Subnets',
                        'ParameterValue': event['Subnets']
                    },
                    {
                        'ParameterKey': 'VPC',
                        'ParameterValue': event['VPC']
                    },
                    {
                        'ParameterKey': 'VolumeSize',
                        'ParameterValue': event['VolumeSize']
                    },
                    {
                        'ParameterKey': 'SSHIP1',
                        'ParameterValue': event['SSHIP1']
                    },
                    {
                        'ParameterKey': 'SSHIP2',
                        'ParameterValue': event['SSHIP2']
                    },
                    {
                        'ParameterKey': 'InstanceProfile',
                        'ParameterValue': event['InstanceProfile']
                    }
                ]
    elif Stage == 'Demo':
        TemplateURL = 'https://s3.amazonaws.com/pimcoreservicetasktemplates/Demo/website-service_DemoV2.yml'
        StackName = 'PimcoreDemoTask' + str(event['Priority'])
        stackParams = [
            { 
                'ParameterKey': 'Priority', 
                'ParameterValue': event['Priority'] 
                
            },
            { 
                'ParameterKey': 'Cluster', 
                'ParameterValue': event['Cluster'] 
                
            },
            { 
                'ParameterKey': 'VPC', 
                'ParameterValue': event['VPC'] 
                
            },
            { 
                'ParameterKey': 'TaskRole', 
                'ParameterValue': event['TaskRole'] 
                
            },
            { 
                'ParameterKey': 'ServiceRole', 
                'ParameterValue': event['ServiceRole'] 
                
            },
            { 
                'ParameterKey': 'HostPattern', 
                'ParameterValue': 'pgsdemo' + event['Priority'] + '.pimcoreclients.com' 
                
            }, 
            { 
                'ParameterKey': 'PROJECT', 
                'ParameterValue': event['Project'] 
                
            },
            { 
                'ParameterKey': 'Stage', 
                'ParameterValue': event['Stage'] 
                
            },
            { 
                'ParameterKey': 'ServiceName', 
                'ParameterValue': event['Project'] +  str(event['Priority'])
                
            },
            { 
                'ParameterKey': 'Listener', 
                'ParameterValue': event['Listener']
                
            } 
        ]
        result['HostPattern'] = 'pgsdemo' + event['Priority'] + '.pimcoreclients.com'
        result['ServiceName'] = event['Project'] +  str(event['Priority'])
        
        
    elif Stage == 'Demo7':
        if 'Flag' in event:
            if event['Flag'] == "DOCKER":
                TemplateURL = 'https://s3.amazonaws.com/pimcoreservicetasktemplates/Demo/website-service_Demo7_V2.yml'
                stackParams = [
                    {
                        'ParameterKey': 'Priority',
                        'ParameterValue': str(event['Priority'])
                    },
                    {
                        'ParameterKey': 'DesiredCount',
                        'ParameterValue': str(event['DesiredCount'])
                    },
                    {
                        'ParameterKey': 'MaxCount',
                        'ParameterValue': str(event['MaxCount'])
                    },
                    { 
                        'ParameterKey': 'Cluster', 
                        'ParameterValue': event['Cluster'] 
                    },
                    {
                        'ParameterKey': 'HostPattern',
                        'ParameterValue': 'pgsdemo7' + str(event['Priority']) + '.pimcoreclients.com'
                    },
                    {
                        'ParameterKey': 'PROJECT',
                        'ParameterValue': event['Project']
                    },
                    { 
                        'ParameterKey': 'Stage', 
                        'ParameterValue': event['Stage'] 
                    },
                    {
                        'ParameterKey': 'ServiceName',
                        'ParameterValue': event['Project'] + str(event['Priority'])
                    },
                    { 
                        'ParameterKey': 'VPC', 
                        'ParameterValue': event['VPC'] 
                
                    },
                    { 
                        'ParameterKey': 'TaskRole', 
                        'ParameterValue': event['TaskRole'] 
                
                    },
                    { 
                        'ParameterKey': 'ServiceRole', 
                        'ParameterValue': event['ServiceRole'] 
                    },
                    { 
                        'ParameterKey': 'Listener', 
                        'ParameterValue': event['Listener']
                    },
                    { 
                        'ParameterKey': 'VolumeSrcPath', 
                        'ParameterValue': event['VolumeSrcPath']
                    },
                    { 
                        'ParameterKey': 'SpecId', 
                        'ParameterValue': event['SpecId']
                    },
                    { 
                        'ParameterKey': 'ImageType', 
                        'ParameterValue': event['ImageType']
                    }
                ]
                result['ServiceName'] = event['Project'] +  str(event['Priority'])
                StackName = 'PimcoreDemo7Task' + str(event['Priority'])
                result['HostPattern'] = 'pgsdemo7' + event['Priority'] + '.pimcoreclients.com'
            else:
                TemplateURL = 'https://s3.amazonaws.com/pimcoreservicetasktemplates/Demo7/Demo7Instances_V1.txt'
                stackParams = [
                    { 
                        'ParameterKey': 'EnvironmentName', 
                        'ParameterValue': event['EnvironmentName'] 
                    },
                    { 
                        'ParameterKey': 'ECSPOCCluster', 
                        'ParameterValue': event['ECSPOCCluster'] 
                    },
                    { 
                        'ParameterKey': 'VPC', 
                        'ParameterValue': event['VPC'] 
                
                    },
                    { 
                        'ParameterKey': 'Stage', 
                        'ParameterValue': event['Stage'] 
                    },
                    { 
                        'ParameterKey': 'Subnets', 
                        'ParameterValue': event['Subnets'] 
                
                    },
                    { 
                        'ParameterKey': 'SecurityGroup', 
                        'ParameterValue': event['SecurityGroup'] 
                
                    },
                    { 
                        'ParameterKey': 'KeyFile', 
                        'ParameterValue': event['KeyFile'] 
                
                    },
                    { 
                        'ParameterKey': 'InstanceType', 
                        'ParameterValue': event['InstanceType'] 
                
                    },
                    { 
                        'ParameterKey': 'ClusterMinSize', 
                        'ParameterValue': event['ClusterMinSize']
                
                    },
                    { 
                        'ParameterKey': 'ClusterMaxSize', 
                        'ParameterValue': event['ClusterMaxSize']
                
                    },
                    { 
                        'ParameterKey': 'VolumeSize', 
                        'ParameterValue': event['VolumeSize']
                
                    },
                    { 
                        'ParameterKey': 'ECSDemo7InstanceProfile', 
                        'ParameterValue': event['ECSDemo7InstanceProfile']
                
                    }
                ]
                StackName = 'PimcoreDemo7Instance' + str(event['Priority'])
        
    try:
        
        response = client.create_stack (
            StackName=StackName,
            TemplateURL=TemplateURL,
            Parameters=stackParams,
            TimeoutInMinutes=5,
            ResourceTypes=resourceTypes,
            OnFailure='DO_NOTHING',
            Tags=[{
                    'Key': 'Env',
                    'Value': event['Stage']
            }],
            ClientRequestToken='string',
            EnableTerminationProtection=False
        )
            
        print (response)
            
        result['StackId'] = response['StackId']
        result['HttpStatus'] = response['ResponseMetadata']['HTTPStatusCode']
        result['Msg'] = 'Stack Creation Initiated Successfully'
        result['StackName'] = StackName
        return result
    except Exception as e:
        result['Msg'] = str(e)
        print (str(e))
        return result