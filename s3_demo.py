"""
from local file upload to bucket
python boto3 upload file to bucket

"""
import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id= 'AKIAR4NDUH53GWDLQFNM',
    aws_secret_access_key='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'
)
# response = s3_client.upload_file(file_name, bucket, object_name)
# response = s3_client.upload_file("Pipfile", "iii-tutorial-v2", "student16/eb103")

"""
from s3 download object to local 
download object from bucket boto3 example
"""


# import boto3

s3 = boto3.client('s3',
                  aws_access_key_id='AKIAR4NDUH53GWDLQFNM',
                  aws_secret_access_key='DHHfSg5PrBysKBzcNaEo2qTWYQksrhTFgPqwNKm7'
                  )

# s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
# s3.download_file('iii-tutorial-v2', 'student16/eb103', 'lbh.txt')

"""
delete the object in s3 bucket
delete object from bucket boto3 example
"""
#s3_client.delete_object(Bucket='examplebucket', Key='objectkey.jpg')
s3_client.delete_object(Bucket='iii-tutorial-v2', Key='student16/eb103')



