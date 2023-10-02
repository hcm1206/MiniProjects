# 정기구독 사용자들을 매 달 결제시키는 프로그램

import schedule
import time
import datetime

# 정기구독 현질한 유저 목록
users = [
    ('김두한', 19), # 김두한은 매 월 19일에 결제
    ('심영', 2), # 심영은 매 월 2일에 결제
    ('상하이조', 29), # 상하이조는 매 월 29일에 결제
    ('이정재', 19), # 이정재는 매 월 19일에 결제
    ('조병옥', 7), # 조병옥은 매 월 7일에 결제
]

# 날짜 확인해서 현질한 유저들의 지갑에서 돈을 빼내는 함수
def pay():
    # 모든 유저에 대하여 확인
    for user in users:
        # 현재 시간 계산
        now = datetime.datetime.now()
        # 현재 날짜(일)이 유저의 결제 일과 같다면
        if now.day == user[1]:
            # 해당 유저의 지갑에서 돈 탈취
            print(user[0] + "님, 결재 실시", now)

# 매일 정각에 pay 함수를 실행하는 스케줄 지정
schedule.every().day.at('00:00').do(pay)

# 1초마다 반복
while True:
    # 현재 지정된 스케줄 중 유효한 스케줄 실행
    schedule.run_pending()
    # 1초 대기
    time.sleep(1)