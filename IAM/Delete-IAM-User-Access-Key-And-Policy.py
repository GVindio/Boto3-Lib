import boto3

def delete_login_profile(username):
    iam = boto3.client('iam')
    try:
        iam.delete_login_profile(UserName=username)
        print(f"Login profile for user {username} deleted successfully.")
    except Exception as e:
        print(f"Error deleting login profile for user {username}: {str(e)}")

delete_login_profile('test')


def delete_access_keys(username):
    iam = boto3.client('iam')
    try:
        keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        for key in keys:
            iam.delete_access_key(UserName=username, AccessKeyId=key['AccessKeyId'])
        print(f"All access keys for user {username} have been deleted.")
    except Exception as e:
        print(f"Error deleting access keys for user {username}: {str(e)}")


def detach_user_policies(username):
    iam = boto3.client('iam')
    try:
        attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        for policy in attached_policies:
            iam.detach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])
        print(f"All policies detached from user {username}.")
    except Exception as e:
        print(f"Error detaching policies from user {username}: {str(e)}")