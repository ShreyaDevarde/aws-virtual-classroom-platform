"""
AWS S3 Service
"""

import boto3
from config import Config


s3_client = boto3.client(
    "s3",
    region_name=Config.AWS_REGION
)


def upload_file(file):
    """
    Upload file to S3 Bucket
    """
    print(
        f"Dummy upload successful: {file.filename}"
    )


def get_all_files():
    """
    Fetch all files from S3 bucket.
    """
    return [
        {"Key": "Python_Basics.pdf"},
        {"Key": "AWS_Introduction.pdf"},
        {"Key": "Machine_Learning_Notes.pdf"}
    ]