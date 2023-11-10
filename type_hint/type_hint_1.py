# 문자열 입력받는 함수

# 소개글 출력 함수 정의(이름, 나이 입력받음)
def introduce(name, age):
    # 입력받은 이름, 나이를 조합하여 소개글 문자열 생성
    greeting_text = "My name is " + name + ".\n" + age + "years old."
    # 생성한 소개글 문자열 출력
    print(greeting_text)