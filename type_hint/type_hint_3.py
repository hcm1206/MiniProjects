# 함수 매개변수에 타입 힌트 추가

# 소개글 출력 함수 정의(이름(문자열 타입), 나이(문자열 타입) 입력받음)
def introduce(name: str, age: str):
    # 입력받은 이름, 나이를 조합하여 소개글 문자열 생성
    greeting_text = "My name is " + name + ".\nI'm " + age + "years old."
    # 생성한 소개글 문자열 출력
    print(greeting_text)

# 소개글 출력 함수에 문자열 이름과 문자열 나이 입력하여 소개글 출력
introduce('Tom', '28')