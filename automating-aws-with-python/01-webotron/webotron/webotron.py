#!/usr/bin/python
# -*- coding: utf-8 -*-


"""Webtron: Deploy websites with aws_secret_access_key
Webotron automates the process of deploying status websites to aws_secret_access_key
- Configure AWS S3 aws_buckets
 - Create them
 - set them up for status website hosting
 - Deploy local files to them
- Configure DNS with AWS Route 53
-Configure a Content Delivery Network and SSL with aws
"""
from pathlib import Path
import mimetypes

import boto3
from botocore.exceptions import ClientError
import click



session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploys websites to AWS"""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets"""
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an s3 bucket"""
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

def upload_file(s3_bucket, path, key):
    content_type = mimetypes.guess_type(key)[0] or 'text/plain'
    s3_bucket.upload_file(
    path,
    key,
    ExtraArgs={
        'ContentType': content_type
    }
    )
@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contects of PATHNAME to BUCKET"""
    s3_bucket = s3.Bucket(bucket)

    root = Path(pathname).expanduser().resolve()
    def handle_directory(target):
        for p in target.iterdir():
            if p.is_dir(): handle_directory(p)
            if p.is_file(): upload_file(s3_bucket, str(p), str(p.relative_to(root)))
    handle_directory(root)

if __name__ == '__main__':
    cli()
