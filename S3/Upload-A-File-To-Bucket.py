import boto3

# Bucket name
BUCKET_NAME = "boto3-lab"

# Initialize the S3 client
s3_client = boto3.client('s3')

def upload_files(file_name, bucket, object_name=None, args=None):
    # If no specific object name is provided, use the file name
    if object_name is None:
        object_name = file_name

    # Attempt to upload the file
    try:
        s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
        print("{} has been uploaded to {} bucket".format(file_name, bucket))
    except Exception as e:
        print("Failed to upload due to {}".format(e))

# File path
file_path = r".\file.txt"

# Call the function with the correct path
upload_files(file_path, BUCKET_NAME)
