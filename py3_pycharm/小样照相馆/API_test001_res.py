from PIL import Image
import requests
import urllib
import io


url = 'http://apicall.id-photo-verify.com/api/take_pic_wm/fe0fb67ac2e711e7a28500163e06132ablue3_wm'
file = io.BytesIO(urllib.request.urlopen(url).read())
img = Image.open(file)
img.show()