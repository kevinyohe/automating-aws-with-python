# coding: utf-8
import boto3
session - boto3.Session(profile_name='pythonAutomation')
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    
    
    print(bucket)
    
    
new_bucket = s3.create_bucket(Bucket='bigtrex1')
new_bucket = s3.create_bucket(Bucket='bigtrex1', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
for bucket in s3.buckets.all():
    
    
    print(bucket)
    
    
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'aws_buckets')
