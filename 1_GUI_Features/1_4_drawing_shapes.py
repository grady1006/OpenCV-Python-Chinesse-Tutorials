import numpy as np
import cv2
import sys

def drawing_shapes(img_path,type):

	img = cv2.imread(img_path)
	if  type =='line':
		cv2.line(img,(100,10),(200,200),(255,255,0),5)
	if  type =='rectangle':
		cv2.rectangle(img,(100,10),(200,200),(255,255,0),5)
	if  type =='circle':
		cv2.circle(img,(180,170),45,(100,100,100),-1)
	if  type =='ellipse':
		cv2.ellipse(img,(256,256),(100,50),0,0,90,255,0)
	if  type =='polylines':
		pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img,[pts],True,(0,0,255))

	cv2.imshow("Drawing",img)
	cv2.waitKey(0)

def add_text(img_path,texts):
	img=cv2.imread(img_path)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,texts,(350,80),font,2,(255,0,0),2,cv2.LINE_AA)
	cv2.imshow("Text",img)
	cv2.waitKey(0)

def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#選擇要畫的形狀
	drawing_shapes("data/opencv.png","circle")
	add_text("data/opencv.png","Hello OpenCV")
if __name__ == '__main__':
    sys.exit(main())


