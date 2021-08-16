import os
from pyminio import Pyminio

pyminio_client = Pyminio.from_credentials(
    endpoint='http://localhost:9000/',
    access_key=os.environ['minioadmin'],
    secret_key=getpass.getpass('minioadmin:')
)

pyminio_client.mkdirs('/test/')

pyminio_client.put_file(
    to_path='/test/',
    file_path=os.path.join(os.getcwd(), 'test.txt')
)
