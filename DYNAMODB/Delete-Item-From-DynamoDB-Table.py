import boto3

# Initialize a DynamoDB resource using the default session
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicCategories')

# Function to delete an item from the table
def delete_item(category_id):
    response = table.delete_item(
        Key={
            'category_id': category_id
        }
    )
    return response

# Category ID of the item to be deleted
category_id_to_delete = 'pop'

# Delete the item and print the response
response = delete_item(category_id_to_delete)
print("Item deleted from DynamoDB table:", response)