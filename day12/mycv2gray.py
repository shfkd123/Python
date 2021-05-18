import cv2



filename = "aaa.jpg"        # 파일 이름과 경로



# 이미지 파일 읽어오기

img_src = cv2.imread(filename)        

# 흑백 명암(그레이스케일)으로 이미지를 변환
img = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY) 



# 아래 줄처럼 이미지를 가져오면서 그레이스케일 처리하는 방법도 있다. 
#  img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)



# 첫 번째 윈도우 생성한다.

cv2.namedWindow("image viewer1", cv2.WINDOW_NORMAL)

# 이미지 원본을 보여준다.
cv2.imshow("image viewer1", img_src)  



# 두 번째 윈도우 생성한다.

cv2.namedWindow("image viewer2", cv2.WINDOW_NORMAL)

# 변환된 이미지를 보여준다.
cv2.imshow("image viewer2", img)  



# 10초 기다린다.

# 단 스페이스바, 엔터 키 등이 입력되면 바로 종료한다.
cv2.waitKey(10000)  

# 이미지 윈도우를 닫고 종료한다.
cv2.destroyAllWindows()   