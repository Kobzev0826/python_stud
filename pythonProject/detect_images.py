import torchvision
import torch
import argparse
import cv2
import detect_utils
import numpy as np
from PIL import Image
import os

'''# construct the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='path to input image/video')
parser.add_argument('-m', '--min-size', dest='min_size', default=800,
                    help='minimum input size for the RetinaNet network')
parser.add_argument('-t', '--threshold', default=0.6, type=float,
                    help='minimum confidence score for detection')
args = vars(parser.parse_args())
print('USING:')
print(f"Minimum image size: {args['min_size']}")
print(f"Confidence threshold: {args['threshold']}")'''

min_size = 1280
threshold = 0.3


# download or load the model from disk
model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=True,
                                                            min_size = min_size)
                                                            #min_size=args['min_size'])
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# load the model onto the computation device
model.eval().to(device)

image_name = 'right_side.jpg'

image = Image.open(image_name).convert('RGB')
# a NumPy copy for OpenCV functions
image_array = np.array(image)
# convert to OpenCV BGR color format
image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

# get the bounding boxes and class labels
boxes, classes = detect_utils.predict(image, model, device, threshold)#args['threshold'])

print(len(boxes))
for i in range(len(boxes)):
    print(boxes[i],classes[i])


# get the final image
result = detect_utils.draw_boxes(boxes, classes, image_array)
dir = os.getcwd()
print(dir)

cv2.imshow('Image', result)
cv2.waitKey(0)
save_name = f"image_name"#f"{args['input'].split('/')[-1].split('.')[0]}_{args['min_size']}_t{int(args['threshold']*100)}"
#cv2.imwrite(f"outputs/{save_name}.jpg", result)
cv2.imwrite(str (image_name.split('.')[1]) + 'conv_Image.jpg',result)