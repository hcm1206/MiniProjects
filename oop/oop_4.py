# 직업 클래스의 상위(부모) 클래스 정의하여 상속

# Person(사람) 상위 클래스 정의
class Person:
    # 클래스 생성자 정의(이름 입력받음)
    def __init__(self, name):
        # 입력받은 이름을 객체 속성으로 저장
        self.name = name

    # 객체 속성(이름)을 이용하여 소개글 출력하는 메서드 정의
    def introduce(self):
        print(f"저는 {self.name}입니다.")


# 사람 클래스를 상속받는 Developer(개발자) 클래스 정의
class Developer(Person):
    # 클래스 생성자 정의(이름 입력받음)
    def __init__(self, name):
        # 상위(사람) 클래스 생성자 호출(이름 입력)
        super().__init__(name)
    
    # 개발자 고유의 코딩 메서드 정의
    def coding(self):
        print(f"{self.name}은 코딩을 합니다.")


# 사람 클래스를 상속받는 Singer(가수) 클래스 정의
class Singer(Person):
    # 클래스 생성자 정의(이름 입력받음)
    def __init__(self, name):
        # 상위(사람) 클래스 생성자 호출(이름 입력)
        super().__init__(name)

    # 가수 고유의 노래 메서드 정의
    def sing(self):
        print(f"{self.name}은 노래를 합니다.")


# 사람 클래스를 상속받는 SoccerPlayer(축구선수) 클래스 정의
class SoccerPlayer(Person):
    # 클래스 생성자 정의(이름 입력받음)
    def __init__(self, name):
        # 상위(사람) 클래스 생성자 호출(이름 입력)
        super().__init__(name)

    # 축구선수 고유의 축구 메서드 정의
    def play_soccer(self):
        print(f"{self.name}은 축구를 합니다.")


# '김철수'라는 이름의 개발자 객체 생성
p1 = Developer('김철수')
# '빌게이츠'라는 이름의 개발자 객체 생성
p2 = Developer('빌게이츠')
# '아이유'라는 이름의 가수 객체 생성
p3 = Singer('아이유')
# 'BTS'라는 이름의 가수 객체 생성
p4 = Singer('BTS')
# '손흥민'이라는 이름의 축구선수 객체 생성
p5 = SoccerPlayer('손흥민')
# '황희찬'이라는 이름의 축구선수 객체 생성
p6 = SoccerPlayer('황희찬')

# 김철수 개발자 소개글 출력
p1.introduce()
# 김철수 개발자 코딩 수행
p1.coding()
# 빌게이츠 개발자 소개글 출력
p2.introduce()
# 빌게이츠 개발자 코딩 수행
p2.coding()
# 아이유 가수 소개글 출력
p3.introduce()
# 아이유 가수 노래 수행
p3.sing()
# BTS 가수 소개글 출력
p4.introduce()
# BTS 가수 노래 수행
p4.sing()
# 손흥민 축구선수 소개글 출력
p5.introduce()
# 손흥민 축구선수 축구 수행
p5.play_soccer()
# 황희찬 축구선수 소개글 출력
p6.introduce()
# 황희찬 축구선수 축구 수행
p6.play_soccer()