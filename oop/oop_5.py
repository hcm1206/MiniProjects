# 직업 클래스 고유 속성 추가

# Person(상위) 사람 클래스 정의
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
    # 클래스 생성자 정의(이름, 언어 입력받음)
    def __init__(self, name, language):
        # 상위(사람) 클래스 생성자 호출(이름 입력)
        super().__init__(name)
        # 입력받은 언어를 객체 속성으로 저장
        self.language = language

    # 객체 속성(이름, 언어)을 이용하여 개발자 고유의 코딩 메서드 정의
    def coding(self):
        print(f"{self.name}은 {self.language}으로 코딩을 합니다.")


# 사람 클래스를 상속받는 Singer(가수) 클래스 정의
class Singer(Person):
    # 클래스 생성자 정의(이름, 대표곡 입력받음)
    def __init__(self, name, representative_song):
        # 상위(사람) 클래스 생성자 호출(이름 입력)
        super().__init__(name)
        # 입력받은 대표곡을 객체 속성으로 저장
        self.representative_song = representative_song

    # 객체 속성(이름)을 이용하여 가수 고유의 노래 메서드 정의
    def sing(self):
        print(f"{self.name}은 노래를 합니다.")

    # 객체 속성(대표곡)을 이용하여 가수 고유의 대표곡 출력 메서드 정의
    def show_representative_song(self):
        print(f"{self.name}의 대표곡은 {self.representative_song}입니다.")

# 사람 클래스를 상속받는 SoccerPlayer(축구선수) 클래스 정의
class SoccerPlayer(Person):
    # 클래스 생성자 정의(이름, 소속팀 입력받음)
    def __init__(self, name, team):
        # 상위(사람) 클래스 생성자 호출(이름 입력)
        super().__init__(name)
        # 입력받은 소속팀을 객체 속성으로 저장
        self.team = team

    # 객체 속성(이름)을 이용하여 축구선수 고유의 축구 메서드 정의
    def play_soccer(self):
        print(f"{self.name}은 축구를 합니다.")

    # 객체 속성(소속팀)을 이용하여 축구선수 고유의 소속팀 출력 메서드 정의
    def show_team(self):
        print(f"{self.name}은 {self.team} 소속입니다.")


# 이름이 '김철수', 언어가 '파이썬'인 개발자 객체 생성
p1 = Developer('김철수', '파이썬')
# 이름이 '빌게이츠', 언어가 'C언어'인 개발자 객체 생성
p2 = Developer('빌게이츠', 'C언어')
# 이름이 '아이유', 대표곡이 '좋은날'인 가수 객체 생성
p3 = Singer('아이유', '좋은날')
# 이름이 'BTS', 대표곡이 'Dynamite'인 가수 객체 생성
p4 = Singer('BTS', 'Dynamite')
# 이름이 '손흥민', 소속팀이 '토트넘홋스퍼'인 축구선수 객체 생성
p5 = SoccerPlayer('손흥민', '토트넘홋스퍼')
# 이름이 '황희찬', 소속팀이 '울버햄튼원더러스'인 축구선수 객체 생성
p6 = SoccerPlayer('황희찬', '울버햄튼원더러스')

# 김철수 개발자 소개글 출력
p1.introduce()
# 김철수 개발자의 언어를 이용한 개발 수행
p1.coding()

# 빌게이츠 개발자 소개글 출력
p2.introduce()
# 빌게이츠 개발자의 언어를 이용한 개발 수행
p2.coding()

# 아이유 가수 소개글 출력
p3.introduce()
# 아이유 가수 노래 수행
p3.sing()
# 아이유 가수 대표곡 출력
p3.show_representative_song()

# BTS 가수 소개글 출력
p4.introduce()
# BTS 가수 노래 수행
p4.sing()
# BTS 가수 대표곡 출력
p4.show_representative_song()

# 손흥민 축구선수 소개글 출력
p5.introduce()
# 손흥민 축구선수 축구 수행
p5.play_soccer()
# 손흥민 축구선수 소속팀 출력
p5.show_team()

# 황희찬 축구선수 소개글 출력
p6.introduce()
# 손흥민 축구선수 축구 수행
p6.play_soccer()
# 손흥민 축구선수 소속팀 출력
p6.show_team()
