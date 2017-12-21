import requests
import base64
import json
from PIL import Image
import requests
import urllib
import io

def que():
    url = 'http://apicall.id-photo-verify.com/api/cut_check_pic'

    pic = open('./files/timg2.jpg', 'rb').read()

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
    print("ok")


def res():
    url = 'http://apicall.id-photo-verify.com/api/take_pic_wm/1f665a88c2eb11e7a28600163e06132ablue3_wm'
    file = io.BytesIO(urllib.request.urlopen(url).read())
    img = Image.open(file)
    img.show()

# def zon():
#     que()


# zon()
que()
# res()