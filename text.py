from minio import Minio
from minio.error import ResponseError

from io import BytesIO


host='144.91.120.175:9000'

access_key= 'minio'

secret_key =  'ScalingWeb'


minioClient = Minio(host, access_key=access_key, secret_key=secret_key, secure=False)

text = "my minio content"

bucket = "testing"

content = BytesIO(bytes(text, 'utf-8'))

key = "sample.text"

size = content.getbuffer().nbytes


try:
	minioClient.put_object(bucket,key, content,size)
	print("Done")
	
except ResponseError as err:
	print("error:", err)
	
