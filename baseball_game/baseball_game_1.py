# 숫자 야구 문제 추출 방식

import random

# 0~10 사이 정수 리스트 생성
numbers = list(range(0, 9))
print(numbers)

# 정수 리스트 중 3개 추첨
three_numbers = random.sample(numbers, 3)
print("맞춰야 할 숫자 :", three_numbers)