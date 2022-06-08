from unittest import result
from pyzbar.pyzbar import decode 
from PIL import Image

img = Image.open("C:/Users/Dell/Desktop/Qr code/qrcode1.png")

result = decode(img)
print(result)


