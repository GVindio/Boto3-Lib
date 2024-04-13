import boto3
from datetime import datetime

# Initialize a DynamoDB client using the default session
dynamodb = boto3.client('dynamodb')

# Function to create a backup of a DynamoDB table
def create_backup(table_name, backup_name):
    response = dynamodb.create_backup(
        TableName=table_name,
        BackupName=backup_name
    )
    return response

# Generate a backup name with a timestamp
backup_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_MusicCategories_Backup"

# Create the backup and print the response
response = create_backup('MusicCategories', backup_name)
print("Backup creation response:", response)
