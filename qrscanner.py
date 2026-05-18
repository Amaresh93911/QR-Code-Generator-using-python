import qrcode

data = "https://github.com/Amaresh93911"

img = qrcode.make(data)

img.save("myqr.png")

img.show()

print("QR Code Generated Successfully")
