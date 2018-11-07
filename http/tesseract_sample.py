"""
使用tesseract识别简单验证码的示例
"""
import sys
import os
import pytesseract
from PIL import Image
 
 
# 对彩色图片进行灰度化处理
def color2gray(path):
    """

    :param 原图路径:
    :return: 灰度化处理后生成的图片路径
    """
    img = Image.open(path)
    img = img.convert('L')
    img.show()
    # 图片都是由数据组成
    data = img.load()
    w,h = img.size
 
    # 对于黑白图片，像素值值是0 纯黑
    # 像素值255 纯白
    for i in range(w):
        for j in range(h):
            #取出来图片中所有的像素值
            if data[i,j] > 135:
                data[i,j] = 255
            else:
                data[i,j] = 0
    #img.show()
    img_name = os.path.basename(path)
    name, subfix = img_name.split('.')
    gray_img_name = '%s.gray.%s' % (name, subfix)
    gray_img = os.path.join(os.path.dirname(path), gray_img_name)
    print(gray_img)
    img.save(gray_img)
    return gray_img


if __name__ == '__main__':
    if len(sys.argv) > 1:
        imgs = sys.argv[1:]
        for img in imgs:
            gray_img = color2gray(img)
            result = pytesseract.image_to_string(Image.open(gray_img))
            print('算法识别验证码结果：',result)
