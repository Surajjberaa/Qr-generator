import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10, border=4)
print("Enter the Text/Url you want to make QRcode of: ")
qr.add_data(input(""))
qr.make(fit=True)
img= qr.make_image(fill_color="white", back_color="black")
# To save image
img.save("QRcode.png")