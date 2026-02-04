from ultralytics import YOLO
import cv2

model = YOLO(r'/home/yacineh/Documents/Centrale/Challenge_final/models/yolov8m-seg.pt')

image = cv2.imread("images/box.jpg")
image = cv2.resize(image, (1280,1280))
prediction = model.predict(image, imgsz=(1280, 1280), show=False, save=False)
print(prediction)
# print(model)

