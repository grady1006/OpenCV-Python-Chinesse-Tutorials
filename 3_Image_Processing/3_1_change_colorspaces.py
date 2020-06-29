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
	#指定pix位置x,y
	px = img[100,100]
	print(px) #顯示BGR顏色數值

	#指定 x,y座標上 0 通道到數值
	blue = img[100,100,0] 
	#0:Blue 1:Green 2:Red
	print(blue)


	#指定圖片像素值
	img[100,100] = [0,0,0] #[B,G,R] 
	print(img[100,100])

	#更好的像素讀取編輯方式
	#基於numpy的資料格式指定物件

	print("(10,10)像素的紅色數值",img.item(10,10,2))

	#修改像素值
	print(img.itemset((10,10,2),100))
	print(img.item(10,10,2))

	#檢視影像屬性

	#行、列、通道;圖像長寬與通道數(channels),可以判斷灰階或彩圖
	print(img.shape)
	#像素總量 w*h*c
	print(img.size)
	#像素資料型態 uint8(0~255)
	print(img.dtype)

	#分割圖像區域
	logo = img[10:300,50:315] #y->dy ,x->dx
	
	#分割與合併，色彩通道

	#分割通道
	b,g,r = cv2.split(img)
	
	#也可以陣列指定通道分割
	b = img[:,:,0]
	g = img[:,:,1]
	r = img[:,:,2]
	print(b.shape)

	#指定通道顏色 
	img[:,:,2] = 255 #R全部變成255

	#合併通道
	img_2 = cv2.merge((b,g,r))

	cv2.imshow("b",b)
	cv2.imshow("g",g)
	cv2.imshow("r",r)

	cv2.imshow("Image Show", img)
	cv2.imshow("Image2 Show", img_2)

	cv2.imshow("logo",logo)


	k = cv2.waitKey(0)
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
