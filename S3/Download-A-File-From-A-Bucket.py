import boto3

BUCKET_NAME = "boto3-lab"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(BUCKET_NAME, 'file.txt')

s3_object.download_file('file.txt')

print("File has been downloaded")