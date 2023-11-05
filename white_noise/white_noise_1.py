# GUI 프로그램 창 출력

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
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

# QApplication 객체 생성
app = QApplication(sys.argv)
# 메인 윈도우 객체 생성
window = MainWindow()
# 메인 윈도우 출력
window.show()
# QApplication 실행
app.exec()