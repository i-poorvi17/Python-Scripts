import qrcode
# Data to be encoded
data = 'Hello, World!'
# Generate QR code
img = qrcode.make(data)
# Save the image
img.save('qrcode.png')