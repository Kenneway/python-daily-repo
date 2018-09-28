# display image

import cv2

img = cv2.imread("./animal.jpg", cv2.IMREAD_COLOR )
cv2.namedWindow("Image")
cv2.imshow("Image", img)

print "save press s, exit press esc"
key = cv2.waitKey (0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("wirte.png", img)
    cv2.destroyAllWindows()
