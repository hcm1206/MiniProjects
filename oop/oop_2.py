# 이름, 직업, 성별 값과 소개글 출력 함수를 통합하여 '사람' 클래스로 정의

# Person(사람) 클래스 정의
class Person:
    # 클래스 생성자 정의(이름, 직업, 성별 입력받음)
    def __init__(self, name, job, sex):
        # 입력받은 이름, 직업, 성별을 객체 속성으로 저장
        self.name = name
        self.job = job
        self.sex = sex

    # 객체 속성(이름, 직업, 성별) 값을 이용하여 소개글 출력하는 메서드 정의
    def introduce(self):
        print(f"{self.name}의 직업은 {self.job}이고 성별은 {self.sex}입니다.")

# 1번째 사람의 이름, 직업, 성별을 이용해 사람 객체 생성
p1 = Person('김철수', '개발자', '남자')
# 1번째 사람 객체의 소개글 출력
p1.introduce()

# 2번째 사람의 이름, 직업, 성별을 이용해 사람 객체 생성
p2 = Person('아이유', '가수', '여자')
# 2번째 사람 객체의 소개글 출력
p2.introduce()

# 3번째 사람의 이름, 직업, 성별을 이용해 사람 객체 생성
p3 = Person('손흥민', '축구선수', '남자')
p3.introduce()