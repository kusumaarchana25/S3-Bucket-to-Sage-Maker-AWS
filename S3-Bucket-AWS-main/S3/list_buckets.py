import boto3

def list_buckets():
    #step1: tell Boto3 that theservice used iss3
    #step2: get list of buckets
    #step3: iterate over the list of buckets
    s3_client=boto3.client('s3')
    response=s3_client.list_buckets()
    print('these are buckets accessible by my credentials: ')
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')