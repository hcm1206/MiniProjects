# 정규표현식을 이용하여 주민등록번호 추출

import re

# 파일 로드 및 텍스트 데이터 추출
with open('regex_test1.txt', 'r', encoding='UTF-8') as File:
    data = File.read()

# 원본 텍스트 출력
print(data)

# 숫자가 6번 반복되고 - 문자가 존재하며 숫자가 7번 반복되는 패턴 구조 생성
p = re.compile(r'\d{6}[-]\d{7}')
# data에서 위 p 패턴 구조를 만족시키는 모든 요소를 찾아 리스트로 저장
rrn_list = re.findall(p, data)
# 패턴 구조가 저장된 리스트 내용 출력
print(rrn_list)