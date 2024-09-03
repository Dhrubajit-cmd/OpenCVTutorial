import cv2 as cv

# Rescaling Image File using OpenCV :

# img = cv.imread("/home/dc/Pictures/Wallpapers/evening.png")
# cv.imshow("Picture", img)

def rescaleFrame(frame , scale = 0.2) :
    # This shall work for images,  videos and live video.
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA )

video_path = "/home/dc/Videos/video.mp4"

capture = cv.VideoCapture(video_path)  # Int  0(in place of path) : Refers Webcam , 1 : 1st Camera Connected to our system and so on..
while True :
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow("Video_Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):  # 0xFF==ord('q') -> Says that until 'q' key is pressed the video keeps on running.
        break
capture.release()
cv.destroyAllWindows()

# Another method for changing the res of the video :
def changeRes(width,height):
    # This works just for the Live Video
    capture.set(4,width)
    capture.set(4,height)


# We can use the code below to resize the image :
img = cv.imread("/home/dc/Pictures/Wallpapers/evening.png")
dimensions = (1920,1080)
resize = cv.resize(img, dimensions) # cv.resize helps us resize the image .
cv.imshow("Resized_Image", resize)

cv.waitKey(0)
