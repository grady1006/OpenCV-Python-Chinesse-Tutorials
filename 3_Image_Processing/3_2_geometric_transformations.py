import cv2
import numpy as np
import sys


def scaling(img_path): #影像縮放方法
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#影像放大
	#方法1
	res = cv2.resize(img,None,fx=1.5, fy=1.5, interpolation = cv2.INTER_CUBIC)
	
	#方法2
	height, width = img.shape[:2]
	res2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
	print(img.shape)
	cv2.imshow('res',res)
	cv2.imshow('res2',res2)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 

def translation(img_path): #平移
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#影像平移
	rows,cols = img.shape[:2] 
	#[1,0,tx]
	#[0,1,yx]
	M = np.float32([[1,0,100],[0,1,100]]) #M 矩陣
	dst = cv2.warpAffine(img,M,(cols,rows)) #平移計算
	
	cv2.imshow('dst',dst)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 

def translation(img_path): #平移
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#影像平移
	rows,cols = img.shape[:2] 
	#記得width = columns ;height = rows 避免混淆
	#[1,0,tx]
	#[0,1,yx]
	M = np.float32([[1,0,100],[0,1,100]]) #M 平移矩陣
	dst = cv2.warpAffine(img,M,(cols,rows)) #平移計算 
	
	cv2.imshow('dst',dst)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows() 

def rotation(img_path): #旋轉
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#影像旋轉
	rows,cols = img.shape[:2] 
	#來計算旋轉角度θ,我們要提供個旋轉矩陣
	#OpenCV提供了可以任意旋轉縮放與不同中心點的旋轉
	# cols-1 和 rows-1 找出影像中心點做旋轉
	M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,1) #計算旋轉矩陣;getRotationMatrix2D(rx,ry,θ,scale)
	print("M旋轉矩陣:",M)
	dst = cv2.warpAffine(img,M,(cols,rows))
	
	cv2.imshow('dst',dst)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows()

def affine_transformation(img_path): #任意映射轉換
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#影像任意點映射
	rows,cols = img.shape[:2] 
	pts1 = np.float32([[50,50],[200,50],[50,200]]) #原圖這三個座標點位置
	pts2 = np.float32([[10,100],[200,50],[100,250]]) #映射轉換後的座標點位置,(50,50)->(10,100)
	M = cv2.getAffineTransform(pts1,pts2)
	print(M)
	#投影轉換
	dst = cv2.warpAffine(img,M,(cols,rows))

	
	cv2.imshow('Input',img)
	cv2.imshow('Output',dst)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows()

def perspective_transformation(img_path): #透視轉換變形
	
	img = cv2.imread(img_path)

	if img is None:
		sys.exit("無法讀取影像...")

	#影像透視點轉換變形
	rows,cols = img.shape[:2] 
	#提供至少4個座標點來計算3x3的透視轉換矩陣
	pts1 = np.float32([[0,275],[512,240],[0,295],[512,260]])
	pts2 = np.float32([[0,0],[512,0],[0,100],[512,100]])
	
	#計算3x3矩陣轉換,將場內線轉換成水平直線
	M = cv2.getPerspectiveTransform(pts1,pts2)
	#透視轉換
	dst = cv2.warpPerspective(img,M,(512,100))

	print(M)

	
	cv2.imshow('Input',img)
	cv2.imshow('Output',dst)
	
	k = cv2.waitKey(0)
	cv2.destroyAllWindows()

def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#放大
	scaling("data/tennis.jpg")
	#平移
	translation("data/tennis.jpg")
	#旋轉
	rotation("data/tennis.jpg")
	#映射變形
	affine_transformation("data/tennis.jpg")
	#透視轉換
	perspective_transformation("data/tennis.jpg")

if __name__ == '__main__':
    sys.exit(main())

