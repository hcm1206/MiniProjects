# 사용자 입력 및 스트라이크 볼 판정 로직 설정

import random

# 0~9 범위 정수 리스트 생성
numbers = list(range(0, 10))
print(numbers)

# 정수 리스트 중 맞출 숫자 3개 추첨
three_numbers = random.sample(numbers, 3)
print("맞춰야할 숫자:", three_numbers)

# 사용자 입력 받음
num1, num2, num3 = map(int, input("0-9 사이의 숫자 세 개 입력(중복 안됨). ex) 3 6 9 >>").split())

# 스트라이크, 볼 변수 초기화
strike = 0
ball = 0

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
print(strike, "strike", ball, "ball")
