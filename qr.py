import qrcode

qr = qrcode.QRCode(
    version=1, # Size of the qrcode
    error_correction= qrcode.constants.ERROR_CORRECT_L, ## Handling error in our qr code
    box_size=10, # Size of the boxes
    border=4 # border of boxes
)

qr.add_data("https://www.realmadrid.com/")

img = qr.make_image(fill_color = "green", back_color = "white")
img.save("qrcode.jpg")