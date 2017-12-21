import requests
import base64
import json

url = 'http://apicall.id-photo-verify.com/api/cut_check_pic'

pic = open('./files/timg1.jpg', 'rb').read()

headers = {'Content-Type': 'application/json'}

data = {

    "spec_id": 360,

    "app_key": 'bee250e5c4ae168b15daae3c95960e5d944cd0ab',

    "file": base64.b64encode(pic).decode()}

data_json = json.dumps(data)

response = requests.post(

    url=url,

    headers=headers,

    data=data_json)

print(response.text)