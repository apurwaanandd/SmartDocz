import boto3
import os

def upload_to_s3(file_content, filename):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )
    bucket_name = os.getenv("S3_BUCKET_NAME")
    s3.put_object(Bucket=bucket_name, Key=filename, Body=file_content)
    return f"https://{bucket_name}.s3.amazonaws.com/{filename}"
