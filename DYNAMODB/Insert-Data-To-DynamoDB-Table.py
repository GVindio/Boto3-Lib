import boto3

# Initialize a DynamoDB resource using the default session
dynamodb = boto3.resource('dynamodb')

# Create the table
table = dynamodb.create_table(
    TableName='MusicCategories',
    KeySchema=[
        {
            'AttributeName': 'category_id',  # Partition key
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'category_id',
            'AttributeType': 'S'  # 'S' for string
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table is created
table.wait_until_exists()

# Confirm table creation
print(f"Table {table.table_name} created successfully with status {table.table_status}")


# Function to insert a category into the DynamoDB table
def insert_category(category_id, name, description):
    table = dynamodb.Table('MusicCategories')
    response = table.put_item(
       Item={
            'category_id': category_id,
            'name': name,
            'description': description
        }
    )
    return response

# Example data
categories = [
    {'category_id': 'rock', 'name': 'Rock', 'description': 'A genre of popular music that originated as "rock and roll" in the United States in the 1950s.'},
    {'category_id': 'jazz', 'name': 'Jazz', 'description': 'A music genre that originated in the African-American communities of New Orleans, United States.'},
    {'category_id': 'classical', 'name': 'Classical', 'description': 'Art music produced or rooted in the traditions of Western culture, including both liturgical and secular music.'},
]

# Insert each category into the DynamoDB table
for category in categories:
    response = insert_category(category['category_id'], category['name'], category['description'])
    print(f"Inserted {category['name']}: {response}")
