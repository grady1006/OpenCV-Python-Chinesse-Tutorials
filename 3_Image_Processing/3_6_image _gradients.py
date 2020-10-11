import cv2
import numpy as np
import sys


def lapacian(img_path): 
	
	img = cv2.imread(img_path,0)

	if img is None:
		sys.exit("無法讀取影像...")

	#laplacian
	laplacian = cv2.Laplacian(img,cv2.CV_64F)

	print(laplacian.shape)
	cv2.imshow('laplacian',laplacian)
	cv2.imshow('src',img)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 

def Sobel(img_path): 
	
	img = cv2.imread(img_path,0)

	if img is None:
		sys.exit("無法讀取影像...")
	#sobelx
	sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
	#sobely
	sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

	
	cv2.imshow('sobelx',sobelx)
	cv2.imshow('sobely',sobely)

	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 



def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)
	#影像梯度計算，色彩或強度方向性變化
	#lapacian
	lapacian("data/opencv.png")
	#Sobel
	Sobel("data/opencv.png")

if __name__ == '__main__':
    sys.exit(main())

