import cv2
import sys
import numpy as np

def arithmetic_operations(img1,img2):
	
	#調用cv2.imread()讀取影像
	img_1 = cv2.imread(img1)
	img_2 = cv2.imread(img2)

	print(img_1.shape)

	logo = img_1[0:250,0:250] #y->dy ,x->dx
	robot = img_2[0:250,0:250]
	#調用cv2.imshow() 顯示讀取進來的影像
	cv2.imshow("logo Show", logo)
	cv2.imshow("robot Show", robot)

	#使用cv2.add(x,y) 像素值相加
	x = np.uint8([250])
	y = np.uint8([10])

	print(cv2.add(x,y)) #250+10=260 ->255 直接修正為上限值

	#如直接用np相加
	print(x+y) #250+10=260 % 256 -> 4 輸出為餘數


	#使用cv2.addWeighted(src1,alpha,src2,beta,gamma)兩張影像權重比例乘加
	#dst(I)=saturate(src1(I)∗alpha+src2(I)∗beta+gamma)
	dst = cv2.addWeighted(logo,0.9,robot,0.1,0) # 合成影像
	cv2.imshow("dst",dst)

	cv2.waitKey(0)
	cv2.destroyAllWindows() 




def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#呼叫顯示圖片
	img1_path = "data/opencv.png"
	img2_path = "data/robot.jpg"

	arithmetic_operations(img1_path,img2_path)

if __name__ == '__main__':
    sys.exit(main())
