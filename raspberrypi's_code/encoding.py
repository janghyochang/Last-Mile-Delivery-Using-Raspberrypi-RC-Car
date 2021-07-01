import base64
import io
from PIL import image
import PIL
import os.path

def img_to_txt(filename):
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

# def img_to_base64_str(img):
#     buffered = io.BytesIO()
#     img.save(buffered, format="PNG")
#     buffered.seek(0)
#     img_byte = buffered.getvalue()
#     img_str = "data:image/png;base64," + base64.b64encode(img_byte).decode()
#     return img_str
#
# def img_from_base64_str(msg):
#     msg = msg.replace("data:image/png;base64,", "")
#     msg = base64.b64decode(msg)
#     buf = io.BytesIO(msg)
#     img = Image.open(buf)
#     return img
filename = './AISL2.jpg'
msg = img_to_txt(filename)
print(msg)
img = decode_img(msg)
print("")
print(img)
# img.show()
# img = './AISL.jpg'
# img_str = img_to_base64_str(img)
# img = img_from_base64_str(img_str)
# img.show()