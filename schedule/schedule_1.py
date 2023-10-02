# 매 초 100원 추가하는 프로그램

import schedule
import time
import datetime

# 전역 변수로 사용할 잔액 my_money를 0원으로 초기화
my_money = 0

# 잔액에 100원을 추가하고 현재 시간과 잔액을 출력하는 함수
def earn_money():
    # 현재 시간 계산
    now = datetime.datetime.now()
    # 전역 변수 my_money 사용
    global my_money
    # 잔액에 100원 추가
    my_money += 100
    # 현재 시간과 잔고 출력
    print(now, "잔고:", my_money)

# 매 초마다 earn_money() 함수를 실행하는 스케줄 추가
schedule.every(1).seconds.do(earn_money)

# 무한 루프
while True:
    # schedule에 지정된 모든 스케줄을 확인하여 유효한 스케줄 실행
    schedule.run_pending()
    # 1초 대기
    time.sleep(1)