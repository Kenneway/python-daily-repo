import numpy as np
import urllib
import cv2

# Method 1: opencv, numpy, urllib
def url_to_image(url):
    # download the image
    # convert it to a numpy array
    # and then read it into opencv format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image

urls = [
    "http://123.59.71.95:8081/app/data/idCardPics/toJJ20180809_1/20180620/20180620_1fc7080bb32bd7bdf5ba391bf9409276.jpg",
    "http://123.59.71.95:8081/app/data/idCardPics/toJJ20180809_1/20180620/20180620_1f7a9d830ee7fda58ebe7e05350fd354.jpg"
]

if __name__ == '__main__':

    # loop over the image urls
    for url in urls:
        print "downloading %s" % (url)
        image = url_to_image(url)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


'''
首先要做的就是导入我们必需的包
使用NumPy转换下载的字节序为NumPy数组，
使用urllib来执行实际的网络请求，使用cv2来绑定OpenCV接口。
使用urllib库来打开这个图像链接
然后将这个下载下来的字节序转换为NumPy数组。
至此NumPy数组还是一个1维数组（也就是一个长长的像素链表）
为了将其转换为2维格式，假设每个像素3个通道（意即分别为红，绿，蓝通道）
使用cv.imdecode函数。
最后返回解码出来的图像给调用函数。
'''

