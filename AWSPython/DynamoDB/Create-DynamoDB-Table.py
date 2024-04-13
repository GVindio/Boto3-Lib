import boto3

# Create a DynamoDB service client using the default session
dynamodb = boto3.resource('dynamodb')

# Define the table schema and attributes
table = dynamodb.create_table(
    TableName='Boto3-Lab',
    KeySchema=[
        {
            'AttributeName': 'id',  # Partition key
            'KeyType': 'HASH'  # Primary key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # 'S' for string, 'N' for number
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table is created
table.wait_until_exists()

# Print out some information about the table
print(f"Table {table.table_name} created successfully with status {table.table_status}")
