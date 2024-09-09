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
dilated = cv.dilate(canny_resized, (5,5), iterations = 1) # I even don't know what do the iterations do here : In the cv2.dilate method from OpenCV, the iterations parameter controls how many times the dilation operation is applied to the image.
dilated_resized = cv.resize(dilated, dimensions )
cv.imshow("Dilated Images", dilated_resized)

# Questions :- What is the difference between normal and dilated image . [Why is the difference not easily visible.]
# Answer : Dilated Image have some properties different than the normal image, we can dilate an image using cv2.dilate(img,ksize,iterations) method in Python.
#  Some of it's properties are :
# Bridging Graphs : Dilation can connect nearby objects or fill in small gaps with objects, effectively merging them together. This is used for tasks like joining broken lines or characters in
# text recognition.
# Smoothing Edges : Sharp corners and edges in the original image tend to become smoother and omore rounded after dilation.
# Reduced Noise : Small, isolated noise pixels can be rmeoved or reduced through dilation, as they get merged with  larger foreground objects.

# Eroding  : (it erodes the dilated image to get back the structural part.)
eroded = cv.erode(dilated_resized,(3,3), iterations = 3)
eroded_resized = cv.resize(eroded, dimensions)
cv.imshow("Eroded", eroded_resized)

# Resize Function :
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA) # If making smaller.
cv.imshow("Simple Show",resized)
# If made bigger, cv.INTER_CUBIC {Slower but better} or cv.INTER_LINEAR can work better.

# Cropping :
cropped = img[50:200, 200:400]
            # the_image_to_crop[row_range,column_range]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
cv.destroyAllWindows()


