import random

# 0~9 범위 숫자 중 3개 추출
numbers = list(range(0, 10))
three_numbers = random.sample(numbers, 3)

# 라운드 변수 초기화
round = 1

# 게임 종료까지 반복
while True:
    # 스트라이크, 볼 변수 초기화
    strike = 0
    ball = 0

    # 현재 라운드 출력
    print("\n[" + str(round) + "라운드]\n")

    # 사용자 입력
    num1, num2, num3 = map(int, input("0-9 사이의 숫자 세 개 입력(중복 안됨). ex)3 6 9 >>").split())

    # 스트라이크 판정
    if three_numbers[0] == num1:
        strike += 1
    if three_numbers[1] == num2:
        strike += 1
    if three_numbers[2] == num3:
        strike += 1

    # 볼 판정
    if three_numbers[1] == num1 or three_numbers[2] == num1:
        ball += 1
    if three_numbers[0] == num2 or three_numbers[2] == num2:
        ball += 1
    if three_numbers[0] == num3 or three_numbers[1] == num3:
        ball += 1

    # 스트라이크 볼 출력
    print(strike, "strike", ball, "ball\n")

    # 3 스트라이크 시 게임 종료 및 반복 종료
    if strike == 3:
        print("[게임 끝]", round, "라운드만에 맞추셨습니다.")
        break
    
    # 게임 종료 아니면 라운드 횟수 추가
    round += 1
