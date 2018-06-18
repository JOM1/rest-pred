import boto3
import botocore

# Create an S3 client
s3 = boto3.client('s3',
    use_ssl=False,
    endpoint_url='http://172.17.0.2:9000', aws_access_key_id='G4FTBCO37J96UCHCQ6DP',
    aws_secret_access_key='dfkViHQM8LLjt54XBuLzhrQtCne8OX5hEhBKMn34')

def upload_file(file_data, bucket_name, object_name):
    """
    Uploads a file.

    Args:
        file_data: File data to upload.
        bucket_name: Name of bucket.
        object_name: Name of object.
    Returns:
        Nothing
    """
    try:
        s3.head_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError:
        s3.create_bucket(Bucket=bucket_name)
    s3.upload_fileobj(file_data, bucket_name, object_name)

def get_file(bucket_name, object_name):
    """
    Returns a file.

    Args:
        bucket_name: Name of bucket.
        object_name: Name of object.
    Returns:
        The file.
    """
    return s3.get_object(Bucket=bucket_name, Key=object_name)['Body']
