import boto3

#Method 1: Creating a new bucket in the default region-''eu-west-3''

def create_buckets():
    #step1: tell Boto3 that the service used is s3
    #step2: create the new bucket
    s3_client=boto3.client('s3')
    s3_client.create_bucket(Bucket='bucket_name')
    print('new bucket created')


#Method 2: Creating a new bucket in a specific region

def create_buckets():
    #step1: tell Boto3 that the service used is s3
    #step2: create the new bucket with 'region' specified as parameter
    s3_client=boto3.client('s3',region_name='region')
    location={'LocationConstraint':'region'}
    s3_client.create_bucket(Bucket='bucket_name',CreateBucketConfiguration=location)
    print('new bucket created')
    return True
