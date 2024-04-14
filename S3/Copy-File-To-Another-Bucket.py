
import boto3

s3 = boto3.resource('s3')

copy_source = {
    'Bucket':'boto3-lab',
    'Key':'file.txt'
}

s3.meta.client.copy(copy_source, 'boto3-lab-1', 'file.txt')