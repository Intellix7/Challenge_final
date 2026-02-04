import numpy as np
from inference_sdk import InferenceHTTPClient
import cv2
from PIL import Image
from ultralytics import YOLO

model = YOLO("models/yolo26n.pt")

# This takes AGES without a GPU cluster
# model.train(data="datasets/yolo26-trash-detections/data.yaml", epochs=10, imgsz=640)

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="LnLWBQvqfEuw3RoUhk9O"
)

result = CLIENT.infer("images/box.jpg", model_id="yolov8-trash-detections/6")
print(result)


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

