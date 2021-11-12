import cv2
import numpy as np

blank_image = np.zeros((100,100,3), np.uint8)
cv2.imshow("Blank", blank_image)


cv2.imwrite("/home/ndnupur/Desktop/voronoi/Code/images/test_fff.png", blank_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

#
# def generate_map(w,h):
#     blank_image = np.zeros((h,w,3), np.uint8)
#     cv2.imshow("Blank",blank_image)
#     cv2.imwrite("/home/ndnupur/Desktop/ENPM808/test_final.png", blank_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()