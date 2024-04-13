import boto3

# Initialize a DynamoDB resource using the default session
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicCategories')

# Function to describe the table
def describe_table():
    response = table.meta.client.describe_table(TableName=table.name)
    return response

# Get the table description
table_description = describe_table()

# Print the table description
print("Table Description:")
print(table_description)
