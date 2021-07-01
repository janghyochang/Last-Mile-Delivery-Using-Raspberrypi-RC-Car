import base64
# import sys
import os.path
import io
from PIL import Image
import requests
from collections import OrderedDict
import json
import http.client

# def makeJson(encodedFile):
#    file_data = OrderedDict()
#    file_data["m2m:cin"] = {'con':encodedFile}
#    return json.dumps(file_data,ensure_ascii=False,indent='\t')

# def Send(encoding_str):
#    conn = http.client.HTTPConnection("203.253.128.161", 7579)
#    payload = makeJson(encoding_str)
#    headers = {
#    'Accept': 'application/json',
#    'X-M2M-RI': '12345',
#    'X-M2M-Origin': '{{aei}}',
#    'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
#    }
#    conn.request("POST", "/Mobius/CSS_v1/data", payload, headers)
#    res = conn.getresponse()
#    data = res.read()
#    print(data)
   
def encode_img(filename):
    msg = b"<plain_txt_msg:img>"
    with open(filename, "rb") as imageFile:
        msg = msg + base64.b64encode(imageFile.read())
    msg = msg + b"<!plain_txt_msg>"
    return msg



# encode_str = encode_img('AISL_1.jpg').decode('utf8')
# Send(encode_str)


# def decode_img(msg):
#     msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):
#               msg.find(b"<!plain_txt_msg>")]
#     msg = base64.b64decode(msg)
#     buf = io.BytesIO(msg)
#     img = Image.open(buf)
#     return img



filename = './AISL_1.jpg'
msg = encode_img(filename)
# # sys.stdout=open('encoding_png.txt','w')
# # # img = decode_img(msg)
# # resize=img.resize((720,720))
# # resize.save('./decoding.jpg')
print(msg)
# # print(img)
# # img.show()

# url = "http://203.253.128.161:7579/Mobius/CSS_v1/data"

# payload = "{\n    \"m2m:cin\": {\n        \"con\": \"~\"\n    }\n}"
# headers = {
#   'Accept': 'application/json',
#   'X-M2M-RI': '12345',
#   'X-M2M-Origin': '{{aei}}',
#   'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

