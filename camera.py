import cv2
import os
import sys
from model import FacialExpressionModel
import numpy as np

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX


def video_capt(filepath):
	assert os.path.exists(filepath), "video file path is not valid" + filepath
	video1 = cv2.VideoCapture(filepath)

	length = int(video1.get(cv2.CAP_PROP_FRAME_COUNT))
	return(length)

#if __name__ == '__main__':
#	assert len(sys.argv) == 2, "Number of arguments not equal to 2"
#	video_capt(str(sys.argv[1]))

def picture_capt(filepath):
	assert os.path.exists(filepath), "photo file path is not valid" + filepath
	image1 = cv2.imread(filepath, 0)
	gray_fr = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	return gray_fr.size


#def emotion(filepath):
#	assert os.path.exists(filepath), "file path is not valid" + filepath
#	image1 = cv2.imread(filepath, 0)
#	gray_fr = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#	#faces = facec.detectMultiScale(gray_fr, 1.3, 5)
#	#emotion_predicted = []

#	return("h")


print(picture_capt('ameya.jpeg'))

