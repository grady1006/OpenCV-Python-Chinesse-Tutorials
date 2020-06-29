import cv2
import sys
import numpy as np

def measuring_performance(img1,img2):
	
	e1 = cv2.getTickCount() #起始時間戳
	#調用cv2.imread()讀取影像

	img_1 = cv2.imread(img1)
	img_2 = cv2.imread(img2)

	e2 = cv2.getTickCount() #終止時間戳

	#計算讀取兩張圖片所需時間
	#cv2.getTickFrequency() 回傳number of clock-cycles per second 每秒時脈頻率
	print("讀取兩張影像時間:",(e2-e1)/cv2.getTickFrequency(),"s")

	#開啟基本優化模式，優化使用不同指令集 SSE2,AVX
	#cv2.useOptimized()開啟加速運算

	print("開啟OpenCV運算優化:",cv2.useOptimized())
	cv2.setUseOptimized(False)

	e1 = cv2.getTickCount() #起始時間戳
	res = cv2.medianBlur(img_1,9)

	e2 = cv2.getTickCount() #終止時間戳

	print("影像Blur計算時間:",(e2-e1)/cv2.getTickFrequency(),"s")
	cv2.imshow("res",res)

	#計算統計圖片非零值數速度比較
	robot2gray = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

	#使用OpenCV 計算所需時間
	e1 = cv2.getTickCount() #起始時間戳
	z = cv2.countNonZero(robot2gray)
	e2 = cv2.getTickCount() #終止時間戳
	print("OpenCV 版本時間:",(e2-e1)/cv2.getTickFrequency(),"s")

	#使用Numpy 計算所需時間
	e1 = cv2.getTickCount() #起始時間戳
	z = np.count_nonzero(robot2gray)
	e2 = cv2.getTickCount() #終止時間戳
	print("Numpy 版本時間:",(e2-e1)/cv2.getTickFrequency(),"s")


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

	#算法運算時間計算
	measuring_performance(img1_path,img2_path)

if __name__ == '__main__':
    sys.exit(main())
