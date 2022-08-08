import boto3

def create_buckets():
    #step1: tell Boto3 that the service used is s3
    #step2: specify the filename inour pc with absolute path
    #step3: specify the name of the bucket within which file has to be uploaded
    #step4: alternatively specify the alternative name by which file has to be uploaded to s3
    if store_as is None:
        store_as='file_name'
    s3_client=boto3.client('s3')
    s3_client.upload_file('file_name','bucket',store_as)

