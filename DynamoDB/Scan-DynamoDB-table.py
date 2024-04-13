import boto3

# Initialize a DynamoDB resource using the default session
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicCategories')

# Function to scan all items in the table
def scan_table():
    # Start with no specific start key
    start_key = None
    all_items = []

    # Loop to handle paginated results from scan API call
    while True:
        if start_key:
            # If there is a start key, scan starting from that key
            response = table.scan(ExclusiveStartKey=start_key)
        else:
            # If no start key, scan from the beginning
            response = table.scan()

        # Extend the list with the items from the current page
        all_items.extend(response.get('Items', []))

        # If 'LastEvaluatedKey' is in the response, there are more items to scan
        start_key = response.get('LastEvaluatedKey', None)
        if not start_key:
            break  # If no more items, break the loop

    return all_items

# Perform the scan
items = scan_table()

# Print each item
print("Scanned items from the DynamoDB table:")
for item in items:
    print(item)
