# 버튼에 함수(슬롯) 추가

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtCore import QSize

# QMainWindow 클래스를 상속받아 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    # 클래스 생성자 정의
    def __init__(self):
        # QMainWindow(상위) 클래스 생성자 호출
        super().__init__()
        # 메인 윈도우 타이틀 설정
        self.setWindowTitle("아기 재우기")
        # 메인 윈도우 크기 설정
        self.setFixedSize(QSize(600, 400))
        # QPushButton(버튼) 객체 3개 생성
        self.audio1_btn = QPushButton('백색소음')
        self.audio2_btn = QPushButton('계곡물소리')
        self.audio3_btn = QPushButton('빗소리')

        # 버튼 객체 3개에 각각 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.audio1_btn.clicked.connect(self.audio1_btn_clicked)
        self.audio2_btn.clicked.connect(self.audio2_btn_clicked)
        self.audio3_btn.clicked.connect(self.audio3_btn_clicked)

        # QHBoxLayout(상자형 수평 레이아웃) 객체 생성
        layout = QHBoxLayout()
        # 상자형 수평 레이아웃에 버튼 객체 3개를 추가
        layout.addWidget(self.audio1_btn)
        layout.addWidget(self.audio2_btn)
        layout.addWidget(self.audio3_btn)

        # QWidget(위젯) 객체 생성
        widget = QWidget()
        # 위젯 객체에 상자형 수평 레이아웃 설정
        widget.setLayout(layout)
        # 위젯 객체를 윈도우 중앙에 오도록 설정
        self.setCentralWidget(widget)

    # 버튼 1의 슬롯 함수 정의(버튼이 눌렸다고 터미널에 출력)
    def audio1_btn_clicked(self):
        print("백색소음 버튼이 클릭되었습니다!")
    
    # 버튼 2의 슬롯 함수 정의(버튼이 눌렸다고 터미널에 출력)
    def audio2_btn_clicked(self):
        print("계곡물소리 버튼이 클릭되었습니다!")

    # 버튼 3의 슬롯 함수 정의(버튼이 눌렸다고 터미널에 출력)
    def audio3_btn_clicked(self):
        print("빗소리 버튼이 클릭되었습니다!")

# QApplication 객체 생성
app = QApplication(sys.argv)
# 메인 윈도우 객체 생성
window = MainWindow()
# 메인 윈도우 출력
window.show()
# QApplication 실행
app.exec()