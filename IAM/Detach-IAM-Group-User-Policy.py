import boto3

def detach_group_policy(group_name, policy_arn):
    iam = boto3.client('iam')
    try:
        iam.detach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        print(f"Policy {policy_arn} detached from group {group_name} successfully.")
    except Exception as e:
        print(f"Failed to detach policy from group {group_name}: {str(e)}")

# Example usage
detach_group_policy('RDSAdmins', 'arn:aws:iam::aws:policy/pyFullAccess')
