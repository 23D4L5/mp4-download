import qrcode

img = qrcode.make(input('Enter u url'))

f = open(print('name ur file.png', 'wb'))
img.save(f)
f.close()