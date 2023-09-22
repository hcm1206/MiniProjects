import random

# 1~45 범위 정수 리스트 생성해서 출력
numbers = list(range(1, 46))
print(numbers)

# 1~45 범위 정수 리스트 중 6개의 수를 랜덤으로 뽑아 출력
selected_numbers = random.sample(numbers, 6)
print(selected_numbers)

# 뽑은 6개 랜덤 수를 정렬하여 출력
selected_numbers.sort()
print(selected_numbers)