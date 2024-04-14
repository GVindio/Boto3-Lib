import boto3

BUCKET_NAME = "boto3-lab"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("Listing Filtered File")

for obj in s3_bucket.objects.filter(Prefix="file"):
    print(obj.key)