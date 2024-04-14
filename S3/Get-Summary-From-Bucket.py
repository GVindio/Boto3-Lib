import boto3


s3 = boto3.resource('s3')

object_summary = s3.ObjectSummary("boto3-lab", "file.txt")

print(object_summary.bucket_name)
print(object_summary.key)