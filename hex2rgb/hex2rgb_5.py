# 예외 처리 추가된 16진수 <=> 10진수 색상 변환 프로그램

from itertools import starmap
import sys
import re

# 사용자 입력
user_input = input(
'''[Hex 코드 또는 RGB 색상을 입력해주세요]
- Hex 코드 입력 예시: #123456
- RGB 색상 입력 예시: 18 52 86
>> '''
)

# 사용자 입력이 #으로 시작하면 16진수 -> 10진수 변환으로 인식
if user_input[0] == '#':
    # 16진수 값이 #을 제외하고 숫자/문자가 6개면 정상 입력으로 인식
    if len(user_input) == 7:
        # 각 숫자/문자별로 반복
        for i in user_input[1:]:
            # 각 숫자/문자가 정상적인 16진수 숫자/문자가 아니면 에러
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
                sys.exit('\n[에러] Hex 코드 입력 시에는 0에서 F(f) 이외의 문자/숫자가 포함되어서는 안됩니다.')
        # R, G, B 값 분할하여 튜플 리스트로 전환
        rgb = [(user_input[1:3], 16), (user_input[3:5], 16), (user_input[5:], 16)]
        # 16진수를 10진수로 변환 및 매핑하여 리스트로 변환
        rgb_list = list(starmap(int, rgb))
        # 변환된 10진수 리스트를 튜플로 전환
        rgb_tuple = tuple(rgb_list)
        # 16진수 => 10진수 최종 반환 결과 출력
        print("\n[반환 결과] ", user_input, ' => ', rgb_tuple)
    # 입력된 16진수 숫자/문자 개수가 6개가 아니면 에러
    else:
        sys.exit('\n[에러] Hex 코드 입력 시에는 # 제외 6자리의 hex 코드를 입력해야 합니다.')

# 사용자 입력이 #으로 시작하지 않으면 10진수 -> 16진수 변환으로 인식
else:
    # 입력값 중 1자리 이상의 숫자값 정규식을 찾아 문자열 리스트로 저장
    rgb_str_list = re.findall(r'\d+', user_input)
    # 변환된 문자열 리스트를 정수로 매핑한 후 R,G,B 요소를 나타낸 튜플로 저장
    rgb_tuple = tuple(map(int, rgb_str_list))

    # 만약 튜플 값이 R,G,B를 나타내는 3개가 아니면 잘못된 입력값으로 인식하여 에러
    if len(rgb_tuple) != 3:
        sys.exit('\n[에러] RGB 색상 입력 시에는 숫자 세 개를 입력해야 합니다.')
    
    # 최종 문자열로 저장할 문자열 생성
    hex_code = '#'

    # 각 R,B,G 요소별로 반복
    for i in rgb_tuple:
        # 값이 0~255 사이라면 정상 입력
        if i >= 0 and i <= 255:
            # 10진수 값을 16진수로 변환 후 앞의 0x 문자열 제거
            temp = hex(i)[2:]
            # 변환된 16진수 자리가 1자리면 앞에 0 추가
            if len(temp) == 1:
                temp = '0' + temp
            # 변환된 16진수 값 중 문자를 대문자로 바꾼 후 최종 문자열에 추가
            hex_code += temp.upper()
        # 값이 0~255 사이가 아니면 에러
        else:
            sys.exit('\n[에러] RGB 색상 입력 시에는 0~255 값을 입력해야 합니다.')
    
    # 10진수 => 16진수 최종 반환 결과 출력
    print("\n[반환 결과] ", rgb_tuple, ' => ', hex_code)