import time
import webbrowser
from datetime import datetime

# 나비보벳따우 실행기

# 날짜 계산
launch_date = datetime(2020, 3, 20)
now = datetime.now()
days_from_luanch = now - launch_date

# 메시지로 출력할 문자열(리스트) 설정
message_list = ["'너굴'\n",
                "안녕구리.\n",
                "모여봐요 동물의 숲이 출시한지 " + str(days_from_luanch.days) + "일이 되었어구리!\n",
                "출시 후 동물의 숲이 정말 많은 사랑을 받았어구리.\n",
                "앞으로도 우리 섬을 잘 부탁해구리!\n",
                "그런 의미에서 우리가 준비한 축하곡을 들어줘구리!\n"]

# 문자열의 각 문장들을 1초 간격으로 출력
for message in message_list:
    print(message)
    time.sleep(1)

# 사용자에게 Y 또는 N을 입력받아 그에 맞는 URL주소를 웹브라우저를 통해 접속
while True:
    answer = input("[선택] 제안 수락은 Y, 거절은 N을 입력>>")
    if answer in ['Y', 'y']:
        url1 = 'https://www.youtube.com/watch?v=0E1yOijtIaM'
        webbrowser.open(url1)
        break
    elif answer in ['N', 'n']:
        url2 = 'https://youtu.be/CanEGYCNGI4?si=8DcQhSXBVwQ0X7VB'
        webbrowser.open(url2)
        break
    else:
        print('\n[경고] Y 또는 N을 입력해줘구리...\n')