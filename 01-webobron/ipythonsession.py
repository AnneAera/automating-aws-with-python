# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket)

#in boto3, you need to specify region by LocationConstraint even you specify profile, in AWS cli can take the profile
new_bucket = s3.create_bucket(Bucket='automatingawsbypython-boto3', CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})

for bucket in s3.buckets.all():
    print(bucket)
