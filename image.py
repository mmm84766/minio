from io import BytesIO
import pandas as pd
from numpy import random
import minio
import numpy

# Create the client
client = minio.Minio(
    endpoint="localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

# Create sample dataset
df = pd.DataFrame({
    "a": numpy.random.random(size=1000),
})

# Create a BytesIO instance that will behave like a file opended in binary mode 
feather_output = BytesIO()
# Write feather file
df.to_feather(feather_output)
# Get numver of bytes
nb_bytes = feather_output.tell()
# Go back to the start of the opened file
feather_output.seek(0)

# Put the object into minio
client.put_object(
    bucket_name="datasets",
    object_name="demo.feather", 
    length=nb_bytes,
    data=feather_output
)


