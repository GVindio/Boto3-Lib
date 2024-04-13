import boto3

def attach_policy(policy_arn, username):
    iam = boto3.client('iam')
    try:
        response = iam.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        print("Policy attached successfully.")
    except iam.exceptions.NoSuchEntityException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

attach_policy('arn:aws:iam::aws:policy/pyFullAccess', 'boto3user')