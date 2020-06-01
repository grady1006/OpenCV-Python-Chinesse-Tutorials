import numpy as np
import cv2
import sys


img = np.zeros((512,512,3), np.uint8)


drawing = False # 滑鼠按住狀態改變
mode = True # 改變形狀
ix,iy = -1,-1
# 滑鼠事件 callback

def mouse_callback(event,x,y,flags,param):

	#滑鼠案一下畫一個圈
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)


def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    print(mode)

    #滑鼠按下移動畫圖
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    #滑鼠左鍵放開停止
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	global mode
	# 創建一個滑鼠觸發視窗
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_circle)
	while(1):
	    cv2.imshow('image',img)
	    k = cv2.waitKey(1) & 0xFF

	    #改變畫不同形狀
	    if k == ord('m'):
	        if mode :
	        	mode = False
	        else:
	        	mode = True
	        print("Change model")
	    elif k == 27:
	        break
	cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main())


