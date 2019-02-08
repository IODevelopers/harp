from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import requests
import datetime
import notification
import TkinterInitialScreen
import pickle
import json

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear

TkinterInitialScreen.StartUI()
data=pickle.load(open("Name.txt",'rb'))
print(data)
	
thresh = 0.25
frame_check = 30
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
		if ear < thresh:
			flag += 1
			print (flag)
			if flag >= frame_check:
				now = datetime.datetime.now()
				hour_data = int(now.hour)
				print ("Drowsy at ",hour_data)
				url = "http://192.168.43.138:8000/insert_to_db"
				data = {"userid":1, "time": hour_data}
				headers = {'Content-type': 'application/json'}
				r = requests.post(url, data = json.dumps(data),headers=headers)
				notification.Notify("Feeling tired?","You just dossed off buddy!")
				flag=1
				# print(int(time.time()))
				# print(r)
		else:
			flag = 0
	# cv2.imshow("Frame", frame)
	# key = cv2.waitKey(1) & 0xFF
	# if key == ord("q"):
	# 	break
cv2.destroyAllWindows()