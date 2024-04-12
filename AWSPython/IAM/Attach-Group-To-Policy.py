import boto3

def attach_policy(policy_arn, group_name):
    iam = boto3.client('iam')
    try:
        response = iam.attach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        print("Policy attached successfully to the group.")
    except Exception as e:
        print(f"Failed to attach policy: {str(e)}")

attach_policy('arn:aws:iam::aws:policy/pyFullAccess', 'S3Admins')
