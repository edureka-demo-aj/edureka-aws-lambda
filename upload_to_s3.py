import logging
import boto3
from botocore.exceptions import ClientError
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3', 
                             aws_access_key_id="AKIAWTIKIIVJQS4YF6GG",
                             aws_secret_access_key="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",
                            )
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        objs = s3_client.list_objects_v2(Bucket='lambdademo-1')['Contents']
        last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]
        print("LAST FILE : ", last_added)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
   upload_file("image-2.png", "lambdademo-1") 