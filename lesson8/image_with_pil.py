from PIL import Image
import numpy as np

# 显示图像
im = Image.open("csdn.png").convert("L")
im.show()  # 显示图像


# 图像转为numpy数组
data = np.array(im)
print(data.shape)

# 图像直方图
for i, k in enumerate(im.histogram()):
    if k > 10:
        print(i, k)

# 图像二值化
data = (data > 100) * 255
Image.fromarray(data.astype('uint8')).show()
