import cv2
import sys

def show_image(img_path):
	
	#調用cv2.imread()讀取影像
	img = cv2.imread(img_path)
	#讀取支援的格式：bmp,pbm, pgm, ppm,jpeg, jpg,tiff, tif,png....

	if img is None:
		sys.exit("無法讀取影像...")

	#調用cv2.imshow() 顯示讀取進來的影像
	cv2.imshow("Image Show", img)


	#調用cv2.waitKey()來持續顯示畫面，等待鍵盤輸入 
	#cv2.waitKey() 參數:時間豪秒，0 為永遠
	k = cv2.waitKey(0)

	#當按下's'鍵儲存影像並離開
	if k == ord("s"):

		cv2.imwrite("first_image.jpg", img)
		print("成功轉檔與儲存!")
		cv2.destroyAllWindows() 



def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#呼叫顯示圖片
	show_image("data/opencv.png")

if __name__ == '__main__':
    sys.exit(main())
