import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def upload_file_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        with open(file_name, 'rb') as file:
            s3_client.upload_fileobj(file, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
        return True
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials")
        return False
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False

# Usage example
file_name = 'C:/Users/gvale/OneDrive/Desktop/Boto3-Lib/S3/aws.png'
bucket_name = 'boto3-lab'

# Optionally, specify a different object name in the bucket
object_name = 'destination-name-in-bucket.png'

# Call the function
upload_file_to_s3(file_name, bucket_name, object_name)
