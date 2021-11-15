from boto3.session import session
import os

accessKey = ''
secretKey = ''
bucket = ''

local_input_prefix = 'home/ubuntu/data'
s3_output_prefix = 'stage/stackexchange/stackoverflow/dump/2021'

files = os.listdir(local_input_prefix)

for f in files:
    input_path = os.join(local_input_prefix, f)
    output_path = os.join(s3_output_prefix, f)
    print('Uploading to: '.format(output_path))
    s3s.upload_file(input_path, output_path)
