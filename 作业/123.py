import qrcode
# vCard内容

vstr = """

BEGIN:VCARD

FN:季爽

TEL:13862810574

EMAIL:13862810574@163.com

NOTE:QQ:669042387,

END:VCARD

"""

qr = qrcode.QRCode()

qr.add_data(vstr)

qr.make(fit=True)

img = qr.make_image()# 生成图片

img.save('D:\\csdn66999888二维码.jpg') # 将图片存入指定路径文件