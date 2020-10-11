import cv2
import sys

def webcam_capture(cam_id):
	
	#調用cv2.VideoCapture()讀取影片
	cap = cv2.VideoCapture(cam_id) # 0,1....
	#影片格式支援

	#cv2.namedWindow('frame',cv2.WINDOW_AUTOSIZE)
 
	print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print(cap.get(cv2.CAP_PROP_FPS))


	while cap.isOpened():
	    
	    ret, frame = cap.read()
	    
	    # 正確讀取影像時 ret 回傳 True
	    frame_count=cap.get(cv2.CAP_PROP_POS_FRAMES)
	    if not ret:
	        print("讀取失敗，請確認攝影機連接...")
	        break
	    
	    #轉灰階畫面顯示
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGR565)

	    cv2.imshow('webcam capture', gray)

	    if cv2.waitKey(1) == ord('q'):
	        break
	
	cap.release()
	cv2.destroyAllWindows()
	

def main(argv=None):
	if argv is None:
		argv=sys.argv
	print(argv)
	print('OpenCV 版本:',cv2.__version__)

	#選擇相機ID
	webcam_capture(1)

if __name__ == '__main__':
    sys.exit(main())


