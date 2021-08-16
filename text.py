from minio import Minio
from minio.error import ResponseError

from io import BytesIO


host="192.168.43.74:9000"

access_key="minioadmin"

secret_key = "minioadmin"


minioClient = Minio(host, access_key=access_key, secret_key=secret_key, secure=False)

text = "my minio content"

bucket = "testing"

content = BytesIO(bytes(text, 'utf-8'))

key = "sample.text"

size = content.getbuffer().nbytes


try:
	minioClient.put_object(bucket,key, content,size)
	print("Done")

	

