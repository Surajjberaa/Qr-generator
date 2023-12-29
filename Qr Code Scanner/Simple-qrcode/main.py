import qrcode as qr
print("Enter the Text/Url you want to make QRcode of: ")
img = qr.make(input(""))
img.save("QrImg.png")