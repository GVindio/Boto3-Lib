import boto3



bucket = boto3.resource('s3')

response = bucket.create_bucket(
    Bucket = "boto3-lab",
    ACL="private",



)

print(response)