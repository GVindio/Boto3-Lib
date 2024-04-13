import boto3

def detach_policy(policy_arn, username):
    iam = boto3.client('iam')
    try:
        response = iam.detach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        print("Policy detached successfully.")
    except iam.exceptions.NoSuchEntityException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

detach_policy('arn:aws:iam::139675813056:policy/pyFullAccess', 'boto3user')