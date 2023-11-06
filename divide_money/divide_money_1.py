# 총 금액에서 랜덤으로 금액을 분할하는 알고리즘

import random

# 총 금액 설정
remaining_amount = 85000
# 랜덤 분할할 금액 개수(인원 수) 설정
people = 5

# 랜덤 분할된 금액을 저장할 빈 리스트 생성
money_per_person = []
# 분할 횟수(인원 수 - 1)만큼 반복
for i in range(people-1):
    # 0 부터 현재 남은 금액 사이의 랜덤값 추출
    temp = random.randint(0, remaining_amount)
    # 남은 금액에서 추출된 랜덤값을 뺌
    remaining_amount -= temp
    # 이번에 추출된 랜덤값을 이번 사람의 분할 금액으로 저장
    money_per_person.append(temp)

# 마지막 남은 금액을 마지막 사람의 분할 금액으로 저장
money_per_person.append(remaining_amount)

# 분할된 금액이 저장된 리스트를 각 사람이 지불해야 할 금액으로 출력
print("각 사람이 지불해야할 금액:", money_per_person)
# 분할된 금액의 합을 계산하여 금액 총합 출력
print("총합: ", sum(money_per_person))

# 분할된 금액이 저장된 리스트를 내림차순으로 정렬
money_per_person.sort(reverse=True)
# 내림차순으로 정렬된 리스트를 출력
print("각 사람이 지불해야할 금액(내림차순):", money_per_person)