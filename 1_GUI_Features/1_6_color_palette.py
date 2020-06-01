import numpy as np
import cv2
import sys


def nothing(x):
    pass


def main(argv=None):
    if argv is None:
        argv=sys.argv
    print(argv)
    print('OpenCV 版本:',cv2.__version__)

    img = np.zeros((300,512,3), np.uint8)
    cv2.namedWindow('image')
    #RGB 顏色調整軸0~255
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)
    
    #顯示開關調色結果
    switch = '0 : OFF \n 1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        # 讀取調整軸顏色數值
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')
        
        #確認開啟調色盤顯示
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main())


