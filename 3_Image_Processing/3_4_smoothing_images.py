import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt


def averaging_filter(img_path): #均化濾波器
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#設計一個10*10的2D濾波器，將影像100個pixs數值平均
	kernel = np.ones((10,10),np.float32)/100
	dst = cv2.filter2D(img,-1,kernel)
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 

def gaussian_blur(img_path): #高斯模糊處理
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")
	#去除高斯雜訊，影像邊緣中產生的噪點
	dst = cv2.GaussianBlur(img,(9,9),0)
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 

def median_blur(img_path): #中通濾波器
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")
	#可用於整張影像雜訊抑制，針對隨機造成的細微胡椒雜訊處理
	#透過濾波器中計算原始影像特定值進行取代

	dst = cv2.medianBlur(img,3)
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 


def bilateral_filter(img_path): #雙通濾波器
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")
	#在空間中也採用高斯濾波器，保留邊緣像素變化較大的部分
	#如濾波器周圍像素相似度較高時進行模糊處理

	dst = cv2.bilateralFilter(img,9,75,75)
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 



def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#影像均化濾波
	averaging_filter("data/opencv.png")
	#高斯模糊濾波
	gaussian_blur("data/opencv.png")
	#中通濾波
	median_blur("data/nois.jpg")
	#雙通濾波
	bilateral_filter("data/nois.jpg")

if __name__ == '__main__':
    sys.exit(main())

