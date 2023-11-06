# 금액 랜덤 분할 GUI 프로그램 UI 구성

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QWidget

# QMainWindow 클래스를 상속받는 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    # 클래스 생성자 정의
    def __init__(self):
        # QMainWindow(상위) 클래스 생성자 호출
        super().__init__()

        # 메인 윈도우 타이틀 설정
        self.setWindowTitle("갹출 금액 랜덤 분할")
        # 메인 윈도우 너비 설정
        self.setFixedWidth(600)

        # 금액 입력 표시 QLabel(라벨) 객체 생성
        self.lb_amount = QLabel('금액 입력:')
        # 금액 입력란 QLineEdit(에딧 영역) 객체 생성
        self.qle_amount = QLineEdit()
        # 게임 참여 맴버 입력 표시 QLabel(라벨) 객체 생성
        self.lb_people = QLabel('게임 참여 맴버')
        # 게임 참여 맴버 입력란 QLineEdit(에딧 영역) 객체 생성
        self.qle_people = QLineEdit()
        # 제출 QPushButton(버튼) 객체 생성
        self.btn_submit = QPushButton('제출')
        # 금액 분할 QPushButton(버튼) 객체 생성
        self.btn_divide_amount = QPushButton('금액 분할')
        # 인원 매칭 QPushButton(버튼) 객체 생성
        self.btn_matching_people = QPushButton('인원 매칭')
        # 분할 금액 출력하는 QPlainTextEdit(텍스트 에딧 영역) 객체 생성
        self.qte_amount = QPlainTextEdit()
        # 매칭된 인원 출력하는 QPlainTextEdit(텍스트 에딧 영역) 객체 생성
        self.qte_people = QPlainTextEdit()
        # 리셋 QPushButton(버튼) 객체 생성
        self.btn_reset = QPushButton('리셋')

        # QHBoxLayout(상자형 수평 레이아웃) 1번째 객체 생성 후 게임 참여 입력 영역과 제출 버튼을 추가
        sub_layout1 = QHBoxLayout()
        sub_layout1.addWidget(self.qle_people)
        sub_layout1.addWidget(self.btn_submit)

        # QHBoxLayout(상자형 수평 레이아웃) 2번째 객체 생성 후 금액 분할 버튼과 인원 매칭 버튼을 추가
        sub_layout2 = QHBoxLayout()
        sub_layout2.addWidget(self.btn_divide_amount)
        sub_layout2.addWidget(self.btn_matching_people)

        # QHBoxLayout(상자형 수평 레이아웃) 3번째 객체 생성 후 분할 금액 출력 영역과 매칭 인원 출력 영역 추가
        sub_layout3 = QHBoxLayout()
        sub_layout3.addWidget(self.qte_amount)
        sub_layout3.addWidget(self.qte_people)

        # QVBoxLayout(상자형 수직 레이아웃) 객체(전체 레이아웃) 생성
        layout = QVBoxLayout()
        # 전체 레이아웃에 금액 입력 라벨 추가
        layout.addWidget(self.lb_amount)
        # 전체 레이아웃에 금액 입력란 영역 추가
        layout.addWidget(self.qle_amount)
        # 전체 레이아웃에 게임 참여 맴버 입력 라벨 추가
        layout.addWidget(self.lb_people)
        # 전체 레이아웃에 수평 레이아웃 1(게임 참여 입력 영역, 제출 버튼) 추가
        layout.addLayout(sub_layout1)
        # 전체 레이아웃에 수평 레이아웃 2(금액 분할 버튼, 인원 매칭 버튼) 추가
        layout.addLayout(sub_layout2)
        # 전체 레이아웃에 수평 레이아웃 3(분할 금액 출력 영역, 매칭 인원 출력 영역) 추가
        layout.addLayout(sub_layout3)
        layout.addWidget(self.btn_reset)

        # QWidget(위젯) 객체 추가
        widget = QWidget()
        # 위젯 객체 레이아웃을 전체 레이아웃으로 설정
        widget.setLayout(layout)
        # 위젯 객체를 윈도우 중앙에 오도록 설정
        self.setCentralWidget(widget)

# 현재 코드가 메인으로 실행된 코드라면
if __name__ == '__main__':
    # QApplication 객체 생성
    app = QApplication(sys.argv)
    # 메인 윈도우 객체 생성
    window = MainWindow()
    # 메인 윈도우 출력
    window.show()
    # QApplication 실행
    app.exec()