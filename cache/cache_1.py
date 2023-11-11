# 데코레이터 함수 구현 및 사용

import time

# 인자로 받은 함수 실행 소요 시간을 알려주는 데코레이터 함수 정의
def time_check(func):
    # 데코레이터 wrapper 함수 정의
    def wrapper():
        # 함수 시작 시각 저장
        start = time.time()
        # 인자로 받은 함수 실행
        func()
        # 함수 종료 시각 저장
        end = time.time()
        # 함수 종료 시각에서 함수 시작 시각을 빼서 함수 실행 시간 계산 후 출력
        print(f"{func.__name__} 함수 실행에 {end-start:.2f}초 소요되었습니다.")
    # 데코레이터 wrapper 함수 반환
    return wrapper

# 함수 실행 소요 시간 측정 함수 적용
@time_check
# 실행 시간이 5초 걸리는 함수 정의
def test():
    # 함수 시작 시점 출력
    print("test 함수 시작")
    # 5초 대기
    time.sleep(5)
    # 함수 종료 시점 출력
    print("test 함수 끝")

# 실행 시간이 5초 소요되는 함수 실행
test()