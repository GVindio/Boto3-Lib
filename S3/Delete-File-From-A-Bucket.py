import boto3
from botocore.exceptions import ClientError

# Initialize the S3 client
client = boto3.client('s3')

# Bucket name and key
bucket_name = 'boto3-lab'
key = 'file.txt'

try:
    # Delete a single text file from the specified bucket
    response = client.delete_object(
        Bucket=bucket_name,
        Key=key
    )
    print("Delete Response: ", response)
except ClientError as e:
    # Handle potential errors in deletion
    print("An error occurred: ", e)


# Deleting Multiple Files



# Initialize the S3 client
# client = boto3.client('s3')

# # Bucket name where the objects are stored
# bucket_name = 'boto3-lab'

# # List of text files to delete
# objects_to_delete = [
#     {'Key': 'file.txt'},
#     {'Key': 'myfile.txt'}
# ]

# try:
#     # Delete multiple text files from the specified bucket
#     response = client.delete_objects(
#         Bucket=bucket_name,
#         Delete={
#             'Objects': objects_to_delete
#         }
#     )
#     print("Delete Response: ", response)
# except ClientError as e:
#     # Handle potential errors in deletion
#     print("An error occurred: ", e)

# # Check for deletion errors specifically within the response
# if 'Errors' in response:
#     print("Errors during deletion: ", response['Errors'])
# else:
#     print("All specified files deleted successfully.")
