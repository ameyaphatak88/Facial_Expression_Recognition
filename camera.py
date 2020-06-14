import cv2
import os
import sys

def video_capt(filepath):
	assert os.path.exists(filepath), "video file path is not valid" + filepath
	video1 = cv2.VideoCapture(filepath)

	length = int(video1.get(cv2.CAP_PROP_FRAME_COUNT))
	return(length)

if __name__ == '__main__':
	assert len(sys.argv) == 2, "Number of arguments not equal to 2"
	video_capt(str(sys.argv[1]))

