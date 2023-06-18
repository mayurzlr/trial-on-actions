# importing necessary modules
import requests, zipfile
from io import BytesIO
import os

print("Downloading started")

# Defining the zip file URL
url = "http://ergast.com/downloads/f1db_csv.zip"

# Split URL to get the file name
filename = url.split("/")[-1]

foldername = filename.split(".")[0]

# Downloading the file by sending the request to the URL
req = requests.get(url)
print("Downloading Completed")

# extracting the zip file contents
zipfile = zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall(f"./raw/{foldername}/")

os.system(f"cp ./raw/{foldername}/* ./raw")
os.system(f"rm -r ./raw/{foldername}/*")
