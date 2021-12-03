"""
This is the upload script which requires to specify the AccessKey, SecretKey and the bucket.
"""

from boto3.session import *
import os

AccessKey = ''
SecretKey = ''
bucket = ''

# change the final destination as needed:
s3_output_prefix = 'stage/stackexchange/stackoverflow/dump/2021/posts'

session = Session(aws_access_key_id=AccessKey, aws_secret_access_key=SecretKey)
s3s = session.resource('s3').Bucket(bucket)

local_input_prefix = 'home/ubuntu/data'
file_name = 'Posts.xml'

input_path = os.path.join(local_input_prefix, file_name)
output_path = os.path.join(s3_output_prefix, file_name)
print('Uploading to: {}'.format(output_path))
s3s.upload_file(input_path, output_path)
