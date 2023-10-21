# 영문자, 숫자, 특수문자 조합으로 랜덤 비밀번호 생성

import string
import random

# 새로운 패스워드 저장할 문자열
new_pw = ""

# 영문자 중 랜덤으로 5개 뽑아서 새로운 패스워드에 추가
for i in range(5):
    new_pw += random.choice(string.ascii_letters)

# 숫자 중 랜덤으로 3개 뽑아서 새로운 패스워드에 추가
for i in range(3):
    new_pw += random.choice(string.digits)

# 특수문자 중 랜덤으로 2개 뽑아서 새로운 패스워드에 추가
for i in range(2):
    new_pw += random.choice("!@#$%^&*")

# 영문자, 숫자, 특수문자 추가된 새로운 비밀번호 문자열 출력
print("생성된 랜덤 비밀번호 :", new_pw)

# 문자열에 속한 문자들을 섞어서 새로운 비밀번호 완성 후 출력
new_pw_shuffle = "".join(random.sample(new_pw, len(new_pw)))
print("섞은 후의 랜덤 비밀번호 :", new_pw_shuffle)