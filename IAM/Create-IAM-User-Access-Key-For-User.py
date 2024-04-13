import boto3


# def create_access(username):
#     iam = boto3.client('iam')

#     response = iam.create_access_key(
#         UserName=username
#     )

#     print(response)



# create_access('boto3user')




def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIASBBTTYTANXVFGDVP',
        Status='Inactive',
        UserName='boto3user'

    )


update_access()



