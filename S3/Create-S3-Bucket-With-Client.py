import boto3


client = boto3.client('s3')

response = client.create_bucket(
    Bucket = "boto3-lab-1",
    ACL = "private",

)

print(response)