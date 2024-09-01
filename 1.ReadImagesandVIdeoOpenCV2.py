
import cv2 as cv
import os

img_path = "/home/dc/Pictures/Wallpapers/evening.png"
if not os.path.isfile(img_path) :
    print(f"Error, file {img_path} does not exist or not found. \n")
else :
    img = cv.imread(img_path)
    if img is None :
       print(f"Error unable to read image {img}. \n ")
    else :
       cv.imshow("Day", img)
       cv.waitKey(0)
       cv.destroyAllWindows()


