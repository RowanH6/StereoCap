import cv2 as cv

right_cam = cv.VideoCapture(1)
left_cam = cv.VideoCapture(2) 

count = 0

path = '3Dcoord/capture'#input("path: ")

while True:
    cl, left = left_cam.read()
    cr, right = right_cam.read()

    cv.imshow('right', right)
    cv.imshow('left', left)

    count = count + 1
    print(300 - count)

    if count == 300:
        cv.imwrite(path + '/l3.jpg', left)
        cv.imwrite(path + '/r3.jpg', right)
        break

    key = cv.waitKey(1)
    if key == 27:
        break