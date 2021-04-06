'''import requests
r = requests.get('http://localhost:5000/video_feed')
print(r)'''

import cv2 as cv

camera = cv.VideoCapture(0)
print(camera.read())

