import base64
# import sys
import os.path
import io
from PIL import Image

def encode_img(filename):
    msg = b"<plain_txt_msg:img>"
    with open(filename, "rb") as imageFile:
        msg = msg + base64.b64encode(imageFile.read())
    msg = msg + b"<!plain_txt_msg>"
    return msg

def decode_img(msg):
    msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):
              msg.find(b"<!plain_txt_msg>")]
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    return img



filename = './AISL2.jpg'
msg = encode_img(filename)
# sys.stdout=open('encoding_png.txt','w')
img = decode_img(msg)
resize=img.resize((720,720))
resize.save('./decoding.jpg')
print(msg)
print(img)
img.show()
