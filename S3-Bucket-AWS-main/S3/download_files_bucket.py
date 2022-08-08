import boto3

# s3_client=boto3.client('s3')
# response=s3_client.download_file(Bucket='download-file-from-bucket',Key='\\models\\file_downloaded_S3.csv',Path='C:\\Users\\acer\\Desktop\\S3_Bucket_to_Sage_Maker\\S3\\models\\file_downloaded_S3.csv')


def download_files(bucket_name, path_to_download, save_as=None):
     #step1: tell Boto3 that the service used is s3
    #step2: to download, specify the filename with path of the bucket
    #step3: optionally specify to alternative name as whichfile has to be stored in pc
    s3_client=boto3.client('s3')
    object_to_download=path_to_download
    s3_client.download_file(bucket_name, object_to_download, save_as)

download_files('download-file-from-bucket','C:\\Users\\acer\\Desktop\\S3_Bucket_to_Sage_Maker\\S3\\models', save_as='file_downloaded_S3.csv')