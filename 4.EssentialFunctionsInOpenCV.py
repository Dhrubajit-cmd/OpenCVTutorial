import cv2 as cv

img = cv.imread("/home/dc/Pictures/Wallpapers/evening.png")
dimensions = (1920,1080)
img_resized = cv.resize(img,dimensions)
cv.imshow('Pictures', img_resized)

# Converting an image to greyscale :
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
dimensions_0 = (1920,1080)
grey_resized = cv.resize(grey,dimensions_0)
cv.imshow("Grey", grey_resized)
# Converting gray to bgr/normal image.
# image = cv.imread("/home/dc/Pictures/Wallpapers/Grey.png")
# back_color = cv.cvtColor(image,cv.COLOR_GRAY2BGR)
# cv.imshow("Normal", back_color)

# Blurring an Image :
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)  # Remember, the ksize must always be kept odd.
dimensions_1 = (1920,1080)
blur_resized = cv.resize(blur,dimensions_1)
cv.imshow("Blur", blur_resized)

# Edge Cascade :(Pretty famous in computer vision world)
canny = cv.Canny(img, threshold1 = 120, threshold2 = 180) # We can also write it as : cv.Canny(img, 120,180)
dimensions_2 = (1920,1080)
canny_resized = cv.resize(canny,dimensions_2)
cv.imshow('Canny Images', canny_resized)


# How to Dilate an image using a specific structuring element :
dilated = cv.dilate(grey_resized, (5,5), iterations = 1) # I even don't know what do the iterations do here.
dilated_resized = cv.resize(dilated, dimensions )
cv.imshow("Dilated Images", dilated_resized)

# Questions :- What is the difference between normal and dilated image . [Why is the difference not easily visible.]

cv.waitKey(0)
cv.destroyAllWindows()
