# 10진수 RGB 코드 튜플 설정
rgb = (255, 238, 221)
# 16진수 RGB 코드 저장할 문자열 생성
hex_code = '#'

# 각 10진수 RGB 튜플 중 R, G, B 요소 별로 반복
for i in rgb:
    # 16진수 변환 후 앞의 0x 문자열 부분 제거
    temp = hex(i)[2:]

    # 16진수 코드가 1자리라면 앞자리에 0 추가
    if len(temp) == 1:
        temp = '0' + temp

    # hex_code 문자열에 변환된 16진수 코드를 대문자로 변환 후 추가
    hex_code += temp.upper()

# 최종 변환 결과 출력
print(rgb, ' => ', hex_code)