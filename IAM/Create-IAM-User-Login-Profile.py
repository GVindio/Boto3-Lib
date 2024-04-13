import boto3

# def create_user(username):
#     iam = boto3.client('iam')
#     try:
#         iam.create_user(UserName=username)
#         print(f"User {username} created successfully.")
#     except Exception as e:
#         print(f"Error creating user {username}: {str(e)}")

# create_user('test')


def create_login(username, password):
    iam = boto3.client('iam')
    try:
        login_profile = iam.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=True
        )
        print(f"Login profile created successfully for user {username}.")
    except Exception as e:
        print(f"Failed to create login profile for user {username}: {str(e)}")

# Example usage (ensure to use a secure method to handle the password)
create_login('test', 'YourSecurePassword123!')
