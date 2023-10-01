# 정해진 양식의 텍스트 파일에서 주민등록번호 추출

# 텍스트 파일 로드
with open('regex_test1.txt', 'r', encoding='UTF8') as File:
    data = File.readlines()

# 텍스트 파일 원본 문자열 출력
print(data)

# 주민등록번호 저장할 리스트 생성
rrn_list = []

# 원본 문자열에서 각 줄(1사람의 정보) 별로 나눠서 반복
for line in data:
    # -로 문자열 구분
    line_split = line.split('-')
    print(line_split)

    # 구분된 문자열의 첫번째 부분의 맨 끝에서 6자리 부분을 주민등록번호 앞자리로 추출
    rrn_front = line_split[0][-6:]
    # 구분된 문자열의 두번째 부분의 맨 앞에서 7자리 부분을 주민등록번호 뒷자리로 추출
    rrn_back = line_split[1][:7]
    # 주민등록번호 앞자리와 뒷자리 사이에 - 추가
    rrn = rrn_front + '-' + rrn_back
    # 주민등록번호 리스트에 추출한 주민등록번호 추가
    rrn_list.append(rrn)

# 주민등록번호 리스트 출력
print(rrn_list)
