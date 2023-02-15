from storages.backends.s3boto3 import S3Boto3Storage
from .secret import AWSS3BUCKET

class MediaStorage(S3Boto3Storage):
    location = ""
    bucket_name = AWSS3BUCKET['DEFAULT_FILE_STORAGE']
    region_name = "ap-northeast-2"
    custom_domain = f"s3.{region_name}.amazonaws.com/{bucket_name}"
    file_overwrite = False