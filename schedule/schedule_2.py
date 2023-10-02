# 매 2시간마다 물마실 시간 알리는 프로그램

import schedule
import time
import datetime

# 물 마실 시간이라고 출력하는 함수
def drink_water():
    # 현재 시간 계산
    now = datetime.datetime.now()
    # 현재 시간과 알림 출력
    print(now, "주인님, 물 마실 시간입니다.")

# 매 2시간마다 drink_water 함수를 실행하는 스케줄 추가
schedule.every(2).hours.do(drink_water)

# 무한 반복
while True:
    # 지정된 모든 스케줄을 확인하여 유효한 스케줄 실행
    schedule.run_pending()
    # 1초 대기
    time.sleep(1)