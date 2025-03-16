import boto3
import os
from django.conf import settings

def generate_presigned_url(filename, operation="put_object", expiration=3600):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
    )

    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=operation,
            Params={"Bucket": settings.AWS_STORAGE_BUCKET_NAME, "Key": filename},
            ExpiresIn=expiration
        )
        return url
    except Exception as e:
        print("Error generating pre-signed URL:", e)
        return None