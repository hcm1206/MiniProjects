# RGB 16진수 코드 <-> RGB 10진수 색상값 변환

from itertools import starmap

# 사용자 입력
user_input = input(
'''[Hex 코드 또는 RGB 색상을 입력해주세요]
- Hex 코드 입력 예시: #123456
- RGB 색상 입력 예시: 18 52 86
>> '''
)

# 16진수 -> 10진수 색상 변환
if user_input[0] == '#':
    # R, G, B값 분할 및 튜플 리스트로 변환
    rgb = [(user_input[1:3], 16), (user_input[3:5], 16), (user_input[5:], 16)]
    # 10진수로 변환 및 매핑
    rgb_list = list(starmap(int, rgb))
    # 튜플 전환
    rgb_tuple = tuple(rgb_list)
    # 최종 결과 출력
    print("\n[반환 결과] ", user_input, ' => ', rgb_tuple)

# 10진수 -> 16진수 색상 변환
else:
    # 공백을 기준으로 R, G, B 값 분할
    rgb = user_input.split(" ")
    # 16진수로 변환 및 매핑
    rgb_tuple = tuple(map(int, rgb))

    # 16진수 저장할 문자열 생성
    hex_code = '#'
    
    # R, B, G 요소별로 반복
    for i in rgb_tuple:
        # 16진수 변환 후 앞의 0x 문자열 제거
        temp = hex(i)[2:]
        
        # 16진수 자리수가 1자리면 앞자리에 0 추가
        if len(temp) == 1:
            temp = '0' + temp
        
        # 16진수 대문자로 변환 후 최종 16진수 문자열에 추가
        hex_code += temp.upper()

    # 최종 결과 출력
    print("\n[변환 결과] ", rgb_tuple, ' => ', hex_code)