from  itertools import starmap

# 16진수 RGB코드 설정
hex_code = '#FFEEDD'

# 변환할 R, G, B 부분을 분할하고 튜플로 전환 후 리스트로 병합
rgb = [(hex_code[1:3], 16), (hex_code[3:5], 16), (hex_code[5:], 16)]
# RGB 리스트의 각 튜플들을 int 함수 인자로 넣어 매핑 후 10진수로 변환
rgb_list = list(starmap(int, rgb))
print(rgb_list)

# 10진수로 변환된 RGB 리스트를 튜플로 변환
rgb_tuple = tuple(rgb_list)
print(rgb_list)

# 변환 결과 출력
print(hex_code, ' => ', rgb_tuple)