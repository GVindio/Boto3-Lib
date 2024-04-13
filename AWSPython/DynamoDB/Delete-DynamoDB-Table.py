import boto3

# Create a DynamoDB service client using the default session
dynamodb = boto3.resource('dynamodb')

# Retrieve the table
table = dynamodb.Table('Boto3-Lab')

# Delete the table
table.delete()

# Wait until the table is deleted
table.wait_until_not_exists()

# Print out a confirmation that the table has been deleted
print(f"Table {table.name} deleted successfully.")
