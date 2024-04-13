import boto3

# Initialize a DynamoDB client using the default session
dynamodb = boto3.client('dynamodb')

# Function to update the provisioned throughput of the table
def update_table_throughput(table_name, read_capacity_units, write_capacity_units):
    response = dynamodb.update_table(
        TableName=table_name,
        ProvisionedThroughput={
            'ReadCapacityUnits': read_capacity_units,
            'WriteCapacityUnits': write_capacity_units
        }
    )
    return response

# Specify new throughput settings
new_read_units = 5
new_write_units = 5

# Update the table and print the response
response = update_table_throughput('MusicCategories', new_read_units, new_write_units)
print("Table update response:", response)
