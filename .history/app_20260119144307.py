import os,sys
import certifi
ca=certifi.where()

from dotenv import load_dotenv
load_dotenv()
mangodb_uri=os.getenv("MONGODB_URI")
print(mangodb_uri)
import pymo

