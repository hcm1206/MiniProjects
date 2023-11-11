# 함수에 캐싱 추가

from random import choice
import time
from functools import cache

# 메뉴 입력받아 메뉴와 가격 결과를 출력하는데 1초가 소요되는 메뉴 작업 함수 정의
def make_menu(user_choice):
    # 입력받은 메뉴 확인 및 작업 시작 시점 출력
    print(f"{user_choice}을(를) 만듭니다.")
    # 1초 대기
    time.sleep(1)
    # 입력받은 메뉴와 가격(20000) 딕셔너리 형태로 반환
    return {
        "menu": user_choice,
        "price": 20000,
    }

# 함수에 캐시 처리하여 입력값에 대한 결과값 저장
@cache
# 메뉴 입력받아 메뉴 작업 함수에 입력하여 실행한 결과를 받는 함수 정의
def get_menu(user_choice):
    # 메뉴 작업 함수에 입력받은 메뉴를 입력하여 나온 결과 반환
    return make_menu(user_choice)

# 현재 코드가 메인으로 실행된 코드라면
if __name__ == "__main__":
    # 시작 시점 저장
    start = time.time()
    # 10회 반복
    for i in range(10):
        # 메뉴 중 하나를 임의로 선택하여 주문할 메뉴로 설정
        user_choice = choice(["치킨", "피자", "떡볶이"])
        # 주문 메뉴 확인 및 메뉴 시작 시점 출력
        print(f'{i+1}번째 손님이 {user_choice}을(를) 주문합니다.')
        # 주문 메뉴를 메뉴 작업 함수에 입력하여 나온 결과 딕셔너리 저장
        menu = get_menu(user_choice)
        # 메뉴 작업 완료 후 완료 시점에 메뉴 결과 딕셔너리 출력
        print(f"주문하신 음식 여기 있습니다> {menu}\n")
    # 종료 시점 저장
    end = time.time()
    # 종료 시점에서 시작 시점을 빼서 프로그램 총 소요시간 계산 후 출력
    print(f"총 소요시간: {end-start: .3f} sec")