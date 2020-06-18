import cv2
import sys
import numpy as np

def arithmetic_operations(img1,img2):
	
	#調用cv2.imread()讀取影像
	img_1 = cv2.imread(img1)
	img_2 = cv2.imread(img2)

	print(img_1.shape)

	logo = img_1[35:285,50:300] #y->dy ,x->dx
	robot = img_2[20:270,25:275]
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
	dst = cv2.addWeighted(logo,0.5,robot,0.5,0) # 合成影像 
	cv2.imshow("dst",dst)


	#使用cv2.bitwise__()完成bitwise 位元運算 Bitwise Operations
	#包含AND,OR,NOT,XOR 算法

	rows ,cols ,channels = img_2.shape
	roi = img_1[0:rows,0:cols]

	robot2gray = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
	ret,mask =cv2.threshold(robot2gray,10,255,cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	

	img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
	img2_fg = cv2.bitwise_and(img_2,img_2,mask = mask)
	
	dst = cv2.add(img1_bg,img2_fg)

	img_1[0:rows,0:cols] = dst
	cv2.imshow("res",img_1)



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
