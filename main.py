import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

# This takes AGES without a GPU cluster
# model.train(data="datasets/yolo26-trash-detections/data.yaml", epochs=1, imgsz=1280)
model.train(data="datasets/coco8.yaml", epochs=10)

model.val()

# from datasets import load_dataset_builder
# recycling_builder = load_dataset_builder('viola77data/recycling-dataset')
# recycling_builder
#
# model = ResNet50(weights='imagenet')
#
# img_dic = 'images/'
#
# img_paths = os.listdir(img_dic)
# print(img_paths)
#
# for path in img_paths:
#     img = cv2.imread(img_dic+path)
#     img = cv2.resize(img, (224, 224))  # Resize the image to match the model's input size
#     x = image.img_to_array(img)  # Convert the image to a numpy array
#     x = np.expand_dims(x, axis=0)  # Add a batch dimension
#     x = preprocess_input(x)
#
#     # Make predictions
#     preds = model.predict(x)
#
#     # Decode and display predictions
#     print('Predicted:', decode_predictions(preds, top=3)[0])

