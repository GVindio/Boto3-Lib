import boto3

# Initialize a DynamoDB client using the default session
dynamodb = boto3.client('dynamodb')

# Function to list all DynamoDB tables
def list_all_tables():
    # Start with no specific start table name
    start_table_name = None
    # This list will store all table names
    all_tables = []
    
    # Loop to handle paginated results from list_tables API call
    while True:
        if start_table_name:
            # If there is a start table name, list tables starting from that name
            response = dynamodb.list_tables(ExclusiveStartTableName=start_table_name)
        else:
            # If no start table name, list from the beginning
            response = dynamodb.list_tables()
        
        # Extend the list with the table names from the current batch
        all_tables.extend(response.get('TableNames', []))
        
        # If 'LastEvaluatedTableName' is in the response, there are more tables to list
        if 'LastEvaluatedTableName' in response:
            start_table_name = response['LastEvaluatedTableName']
        else:
            break  # If no more tables, break the loop

    return all_tables

# Get the list of all tables
tables = list_all_tables()

# Print the list of table names
print("List of DynamoDB tables:")
for table in tables:
    print(table)
