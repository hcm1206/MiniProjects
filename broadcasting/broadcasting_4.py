# 매 정오마다 점심시간 안내방송을 출력하는 프로그램

from gtts import gTTS
from playsound import playsound
from datetime import datetime
import schedule
import time

# 점심시간 안내문 설정
text = '''
임직원 여러분 점심시간입니다.
오전 내내 일하시느라 고생하셨습니다.
구내 식당에 맛있는 점심을 준비해놨으니 식사하러 이동하세요.
'''

# 안내문을 한국어 TTS로 변환
tts = gTTS(text, lang='ko')
# 한국어 TTS를 mp3 파일로 저장
tts.save('result.mp3')

# 현재 시간과 방송 시작 여부를 출력하고 방송 내용을 전파하는 함수
def broadcast():
    now = datetime.now()
    print(now, "방송 시작")
    playsound('result.mp3')

# 매일 정오 12시에 broadcast 함수를 실행하는 스케줄 설정
schedule.every().day.at("12:00").do(broadcast)

# 매 1초마다
while True:
    # 설정된 스케줄 중 유효한 스케줄을 체크하여 실행
    schedule.run_pending()
    time.sleep(1)