import boto3

# Initialize a DynamoDB resource using the default session
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicCategories')

# Data for the new category
new_category = {
    'category_id': 'pop',
    'name': 'Pop',
    'description': 'A genre of popular music that originated in its modern form during the mid-1950s in the United States and the United Kingdom.'
}

# Function to add an item to the table
def add_item_to_table(item):
    response = table.put_item(Item=item)
    return response

# Add the new category to the table
response = add_item_to_table(new_category)
print("Item added to DynamoDB table:", response)