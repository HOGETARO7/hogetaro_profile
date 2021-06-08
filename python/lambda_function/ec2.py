import boto3
import json

def lambda_handler(event, context):
    """
    Make list of current instances.
    """
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    
    #インスタンス情報取得
    for reservations in instances['Reservations']:
        for instance in reservations['Instances']:
            
            #インスタンスIDの取得
            target = instance['InstanceId']

            #インスタンスIDの型をリスト型に変換
            target = [target]
            
            #インスタンスを停止する
            ec2.stop_instances(InstanceIds=target)