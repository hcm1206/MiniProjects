# 함수 입력 타입과 함수 로직 불일치 시 에러 발생

# 소개글 출력 함수 정의(이름, 나이 입력받음)
def introduce(name, age):
    # 입력받은 이름, 나이를 조합하여 소개글 문자열 생성
    greeting_text = "My name is " + name + ".\nI'm " + age + " years old."
    # 생성한 소개글 문자열 출력
    print(greeting_text)

# 소개글 출력 함수에 문자열 이름과 정수 나이 입력하여 소개글 출력(타입 불일치로 인한 오류 발생)
introduce("Tom", 28)