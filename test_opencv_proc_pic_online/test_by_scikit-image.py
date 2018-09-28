import cv2
from skimage import io

# Method 2: scikit-image opencv
for url in urls:
    print "downloading %s" % (url)
    image = io.imread(url)
    cv2.imshow("Incorrect", image)
    cv2.imshow("Correct", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)


'''
scikit-image库中做得很漂亮的一点是：
io子库中的imread函数能够区分图像路径到底在磁盘上还是一个URL
不过这里有一个很严重的错误:
OpenCV以BGR顺序表达一幅图像，然而scikit-image则是RGB顺序
如果你使用scikit-iamge的imread函数，
而且还想在下载完成后使用OpenCV的函数，
那么你需要将图像从RBG转换为BGR。
'''

