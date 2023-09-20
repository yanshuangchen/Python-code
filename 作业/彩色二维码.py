'''import qrcode

# 要生成QR码的数据
data = "https://studyvideoh5.zhihuishu.com/stuStudy?recruitAndCourseId=4b5b505e41504859454a585958435b4750"

# 生成QR码对象
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# 添加数据到QR码对象
qr.add_data(data)

# 填充QR码
qr.make(fit=True)

# 生成QR码图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存QR码图片
img.save("D:\\example1.png")'''
import qrcode
from PIL import Image

# 要生成QR码的数据
data = "https://studyvideoh5.zhihuishu.com/stuStudy?recruitAndCourseId=4b5b505e41504859454a585958435b4750"

# 生成QR码对象
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# 添加数据到QR码对象
qr.add_data(data)

# 填充QR码
qr.make(fit=True)

# 生成QR码图片(背景色，前景色)
img = qr.make_image(fill_color="red", back_color="white")

# 添加logo到QR码图片
logo = Image.open(r"C:\Users\86138\Desktop\logohong.png")

# 计算logo的大小
logo_size = img.size[0] // 4
logo_w, logo_h = logo.size
if logo_w > logo_size or logo_h > logo_size:
    logo_w, logo_h = tuple((float(logo_size) / max(logo_w, logo_h)) * dim for dim in (logo_w, logo_h))
    logo = logo.resize((int(logo_w), int(logo_h)))

# 计算logo放置的位置
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

# 将logo放入二维码中
img.paste(logo, pos)
# 保存QR码图片
img.save("D:\\11255example.png")