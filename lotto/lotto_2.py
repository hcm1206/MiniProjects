import random

# 1~45 범위의 정수 리스트 생성
numbers = list(range(1, 46))

# 로또 번호 5번 뽑아서 출력
for i in range(1, 6):
    selected_numbers = random.sample(numbers, 6)
    selected_numbers.sort()
    print(str(i) + "게임 :", selected_numbers)