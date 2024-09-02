
import cv2 as cv
import os

# Reading Images in OpenCV
img_path = "/home/dc/Pictures/Wallpapers/evening.png"
if not os.path.isfile(img_path) :
    print(f"Error, file {img_path} does not exist or not found. \n")
else :
    img = cv.imread(img_path)
    if img is None :
       print(f"Error unable to read image {img}. \n ")
    else :
       cv.imshow("Evening", img)
       cv.waitKey(0)
       cv.destroyAllWindows()


# Reading Videos in OpenCV

video_path = "/home/dc/Videos/video.mp4"

capture = cv.VideoCapture(video_path)  # Int  0(in place of path) : Refers Webcam , 1 : 1st Camera Connected to our system and so on..
while True :
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord('q'):  # 0xFF==ord('q') -> Says that until 'q' key is pressed the video keeps on running.
        break
capture.release()
cv.destroyAllWindows()





