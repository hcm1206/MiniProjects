# GUI 프로그램에 버튼 추가

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
        self.audio1_btn = QPushButton('백색소움')
        self.audio2_btn = QPushButton('계곡물소리')
        self.audio3_btn = QPushButton('빗소리')

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

# QApplication 객체 생성
app = QApplication(sys.argv)
# 메인 윈도우 객체 생성
window = MainWindow()
# 메인 윈도우 출력
window.show()
# QApplicatoin 실행
app.exec()