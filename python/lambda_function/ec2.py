
import boto3

region = 'ap-northeast-1'

def lambda_handler(event, context):

    ec2 = boto3.client('ec2', region_name=region)
    responce = ec2.describe_instances()

    ec2.stop_instances(InstanceIds=responce)
    print('stopped instances: ' + str(instances))