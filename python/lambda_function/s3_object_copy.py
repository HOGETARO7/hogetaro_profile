import json
import boto3
import urllib.parse

s3 = boto3.resource('s3')

def lambda_handler(event, context):

    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
        
    copy_source = {
    'Bucket': bucket,
    'Key': key
    }
    
    print(bucket)
    print(key)
    
    try:
        s3.meta.client.copy(copy_source,Bucket='yotaro-backup-bucket',Key=key)
                       
    except ClientError as e:
        logging.error(e)
        return False
        
    return True