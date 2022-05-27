import cv2
import dlib
import os
import imutils
from imutils import face_utils
from imutils.video import VideoStream
from imutils.face_utils import rect_to_bb
from imutils.face_utils import FaceAligner

def create_dataset():

	sampleNum = 0
	vs = VideoStream(src=0).start()
	# Capturing the faces one by one and detect the faces and showing it on the window
	while(True):
		# Capturing the image
		#vs.read each frame
		frame = vs.read()
		cv2.imshow("Add Images",frame)
		if cv2.waitKey()==27:
			break
		sampleNum += 1
	#Stoping the videostream
	vs.stop()
	# destroying all the windows
	cv2.destroyAllWindows()