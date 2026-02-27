import qrcode as qr
img = qr.make("https://www.mbust.edu.np/")
img.save("mbust.png")