import cv2 as cv
import numpy as np

# Creating a blank image

blank = np.zeros((500,500,3), dtype = "uint8") # The three digits mean the (height,width,color channel))
cv.imshow("Blank", blank)
img = cv.imread("/home/dc/Pictures/Wallpapers/evening.png")
blank[200:300,300:400] = 0,0,255 # [:] Basically gives us a range of pixels. And the other part gives us the color.
cv.imshow('Green', blank)

# Draw a rectangle :
cv.rectangle(blank, (0,0),(250,500),(0,0,255), thickness = cv.FILLED)
# We can fill this rectangle using thickness = cv.FILLED or we can give -1.

cv.imshow("Rectangle", blank)

# Draw a circle :

cv.circle(blank, (250,250), 40 , (0,255,0), thickness = cv.FILLED)
cv.imshow("Circle", blank)

# Draw a Line :
cv.line(blank, (0,0), (250,250), (255,0,0))
cv.imshow("Line", blank)

# Write a text :
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_PLAIN, 1.0, (255,0,0), 2 )
cv.imshow("TEXT", blank)
cv.waitKey(0)
cv.destroyAllWindows()


# SATURDAY AUR SUNDAY INN DO DIN MEIN KHATAM KARNI HI HAIN !!

