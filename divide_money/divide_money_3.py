# GUI 프로그램 로직 구현

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QWidget
import random

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

        # 총 금액을 나타내는 변수를 생성하고 초기화
        self.amount = 0
        # 인원을 나타내는 빈 리스트 생성
        self.people = []
        # 금액 분할 클릭 횟수를 나타내는 변수를 생성하고 초기화
        self.btn_divide_amount_clicked_cnt = 0

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

        # 금액 입력란 에딧 영역의 내용이 바뀔 때(시그널) 실행할 함수(슬롯) 설정
        self.qle_amount.textChanged.connect(self.amount_changed)
        # 제출 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.btn_submit.clicked.connect(self.btn_submit_clicked)
        # 금액 분할 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.btn_divide_amount.clicked.connect(self.btn_divide_amount_clicked)
        # 인원 매칭 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.btn_matching_people.clicked.connect(self.btn_matching_people_clicked)
        # 리셋 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.btn_reset.clicked.connect(self.btn_reset_clicked)

        # 초기에 금액 분할 버튼과 인원 매칭 버튼을 비활성화
        self.btn_divide_amount.setEnabled(False)
        self.btn_matching_people.setEnabled(False)

        # QHBoxLayout(상자형 수평 레이아웃) 객체를 서브 레이아웃 1로 생성 후 게임 참여 맴버 입력 영역과 제출 버튼을 추가
        sub_layout1 = QHBoxLayout()
        sub_layout1.addWidget(self.qle_people)
        sub_layout1.addWidget(self.btn_submit)

        # QHBoxLayout(상자형 수평 레이아웃) 객체를 서브 레이아웃 2로 생성 후 게임 참여 맴버 입력 영역과 제출 버튼을 추가
        sub_layout2 = QHBoxLayout()
        sub_layout2.addWidget(self.btn_divide_amount)
        sub_layout2.addWidget(self.btn_matching_people)

        # QHBoxLayout(상자형 수평 레이아웃) 객체를 서브 레이아웃 3로 생성 후 분할 금액 출력 영역과 매칭 인원 출력 영역 추가
        sub_layout3 = QHBoxLayout()
        sub_layout3.addWidget(self.qte_amount)
        sub_layout3.addWidget(self.qte_people)

        # QVBoxLayout(상자형 수직 레이아웃) 객체를 전체 레이아웃으로 생성
        layout = QVBoxLayout()
        # 전체 레이아웃에 금액 입력 표시 라벨 추가
        layout.addWidget(self.lb_amount)
        # 전체 레이아웃에 금액 입력란 에딧 영역 추가
        layout.addWidget(self.qle_amount)
        # 전체 레이아웃에 게임 참여 맴버 입력 표시 라벨 추가
        layout.addWidget(self.lb_people)
        # 전체 레이아웃에 서브 레이아웃 1 추가
        layout.addLayout(sub_layout1)
        # 전체 레이아웃에 서브 레이아웃 2 추가
        layout.addLayout(sub_layout2)
        # 전체 레이아웃에 서브 레이아웃 3 추가
        layout.addLayout(sub_layout3)
        # 전체 레이아웃에 리셋 버튼 추가
        layout.addWidget(self.btn_reset)

        # QWidget(위젯) 객체 추가
        widget = QWidget()
        # 위젯 객체 레이아웃을 전체 레이아웃으로 설정
        widget.setLayout(layout)
        # 위젯 객체를 윈도우 중앙에 오도록 설정
        self.setCentralWidget(widget)

    # 금액 입력란 에딧 영역 슬롯 함수 정의(금액 입력란의 값을 amount로 입력받음)
    def amount_changed(self, amount):
        # 변경된 금액 출력
        print(amount)
        # 총 금액을 현재 변경된 금액 입력란의 값으로 저장
        self.amount = amount
    
    # 제출 버튼 슬롯 함수 정의
    def btn_submit_clicked(self):
        # 게임 참여 맴버 입력란에 입력된 값을 텍스트(문자열) 형식으로 로드
        self.people_str = self.qle_people.text()
        # 게임 참여 맴버 문자열을 콤마(,)를 기준으로 구분하여 리스트로 변환
        self.people = self.people_str.split(',')
        # 게임 참여 맴버 리스트 출력
        print(self.people)
        # 게임 참여 맴버가 모두 결정되었으므로 금액 분할 버튼 활성화
        self.btn_divide_amount.setEnabled(True)

    # 금액 분할 버튼 슬롯 함수 정의
    def btn_divide_amount_clicked(self):
        # 클릭 시마다 금액 분할 클릭 횟수를 1씩 증가
        self.btn_divide_amount_clicked_cnt += 1
        # 현재 총 금액을 정수형으로 변경
        self.amount = int(self.amount)

        # 이번 금액 분할 횟수가 참여 인원 수보다 적다면(이번 금액 분할이 마지막이 아니라면)
        if self.btn_divide_amount_clicked_cnt < len(self.people):
            # 0 ~ 남은 총 금액 사이의 랜덤 정수값 추출
            temp = random.randint(0, self.amount)
            # 총 금액에서 추출한 정수값을 뺌
            self.amount -= temp
            # 분할 금액 출력 영역에 추출한 정수값을 문자열로 하여 추가 후 표시
            self.qte_amount.appendPlainText(str(temp))
        # 이번 금액 분할 횟수가 참여 인원 수와 같다면 (이번 금액 분할이 마지막 분할이라면)
        elif self.btn_divide_amount_clicked_cnt == len(self.people):
            # 분할 금액 출력 영역에 현재 총 금액을 문자열로 하여 추가 후 표시
            self.qte_amount.appendPlainText(str(self.amount))
            # 금액 분할이 모두 끝났으므로 인원 매칭 버튼을 활성화
            self.btn_matching_people.setEnabled(True)

    # 인원 매칭 버튼 슬롯 함수 정의
    def btn_matching_people_clicked(self):
        # 현재 참여 인원 수가 0보다 크다면
        if len(self.people) > 0:
            # 참여 인원을 랜덤으로 셔플
            random.shuffle(self.people)
            # 참여 인원 리스트의 마지막 원소(인원)을 추출하고 리스트에서 제거
            temp = self.people.pop()
            # 매칭 인원 출력 영역에 추출된 인원을 문자열로 하여 추가 후 표시
            self.qte_people.appendPlainText(str(temp))

    # 리셋 버튼 슬롯 함수 정의
    def btn_reset_clicked(self):
        # 총 금액을 다시 0으로 초기화
        self.amount = 0
        # 참여 인원 리스트 원소 모두 제거
        self.people = []
        # 분할 버튼 클릭 횟수를 다시 0으로 초기화
        self.btn_divide_amount_clicked_cnt = 0

        # 금액 입력란에 입력된 값 모두 제거
        self.qle_amount.clear()
        # 게임 참여 인원 입력란에 입력된 값 모두 제거
        self.qle_people.clear()
        # 분할 금액 에딧 영역에 출력된 값 모두 제거
        self.qte_amount.clear()
        # 인원 매칭 에딧 영역에 출력된 값 모두 제거
        self.qte_people.clear()

        # 금액 분할 버튼을 다시 비활성화
        self.btn_divide_amount.setEnabled(False)
        # 인원 매칭 버튼을 다시 비활성화
        self.btn_matching_people.setEnabled(False)

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