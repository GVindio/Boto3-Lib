import boto3

# Initialize a DynamoDB resource using the default session
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicCategories')

# Function to delete all items from the table
def delete_all_items():
    # Scan the table
    response = table.scan()
    items = response.get('Items', [])
    
    # Continue scanning if all items were not returned
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response.get('Items', []))
    
    # Use batch writer for more efficient deletion
    with table.batch_writer() as batch:
        for item in items:
            batch.delete_item(
                Key={
                    'category_id': item['category_id']
                }
            )

    print(f"Deleted {len(items)} items from the table.")

# Call the function to delete all items
delete_all_items()