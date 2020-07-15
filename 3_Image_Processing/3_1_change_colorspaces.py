import cv2
import numpy as np
import sys

def segmentation_tennis(img_path):
	
	#調用cv2.imread()讀取影像
	img = cv2.imread(img_path)
	#讀取支援的格式：bmp,pbm, pgm, ppm,jpeg, jpg,tiff, tif,png....

	if img is None:
		sys.exit("無法讀取影像...")
	#色彩空間轉換 BGR 轉 HSV
	#我們要將黃色網球分割出來
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	#來找出正黃色RGB值在HSV的數值
	yellow = np.uint8([[[0,255,255 ]]]) #BGR
	hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
	print( hsv_yellow ) #[[[ 30, 255, 255]]] H:色調 S:飽和度 V:亮度,正黃色的位置30 255,255 

	# 在HSV的色彩空間中定義黃色區間,這樣就可以初步分出網球的位置
	lower_yellow = np.array([25,100,80])
	upper_yellow = np.array([40,255,255])

	# 將圖像中色彩分割黃色區間出來的遮罩
	mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	
	# 遮罩跟原圖做AND取出分割的影像
	res = cv2.bitwise_and(img,img, mask= mask)
	cv2.imshow('frame',img)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 



def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#分割
	segmentation_tennis("data/tennis.jpg")

if __name__ == '__main__':
    sys.exit(main())

