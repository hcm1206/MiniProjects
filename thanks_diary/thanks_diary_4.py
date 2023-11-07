# 감사제목 수정/삭제 옵션 UI 추가

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, \
    QLineEdit, QPushButton, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
import sqlite3
import pandas as pd

# 데이터베이스에서 데이터를 읽어와 데이터 프레임을 반환하는 함수
def read_data():
    # thanks.db(감사 제목 DB) sqlite3 데이터베이스를 연동하여 con으로 저장
    with sqlite3.connect("thanks.db") as con:
        # 감사 제목 DB의 커서 객체 생성
        cur = con.cursor()
        # 감사 제목 DB의 인덱스, 내용, 생성 날짜 조회 쿼리문 실행
        cur.execute('''
        SELECT idx, content, created_at FROM thanks_list ORDER BY idx DESC;            
        ''')
        # 실행된 쿼리문 결과 저장
        result = cur.fetchall()

    # 칼럼명 저장할 빈 리스트 생성
    cols = []
    # 감사 제목 DB의 칼럼명들을 칼럼명 리스트에 별도로 저장
    for column in cur.description:
        cols.append(column[0])
    
    # 감사 제목 DB의 내용과 칼럼명 리스트를 데이터 프레임 형식으로 저장
    thanks_list = pd.DataFrame.from_records(data=result, columns=cols)
    # 저장된 데이터 프레임 출력
    print(thanks_list)

    # 데이터 프레임 리턴
    return thanks_list

# 데이터 프레임 내용을 UI 테이블에 출력하는 함수
def show_data(thanks_list, table):
    # 테이블의 행 수를 감사 제목 데이터 프레임의 행 수로 설정
    table.setRowCount(len(thanks_list))

    # 반복 변수 i를 이용하여 감사 제목 데이터 프레임의 내용(행)마다 반복
    for i in range(len(thanks_list)):
        # 감사 제목 데이터 프레임의 i번째 행 0번째 열(인덱스) 내용을 추출
        idx = QTableWidgetItem(str(thanks_list.iloc[i, 0]))
        # 추출한 인덱스를 테이블의 i번째 행 0번째 열로 설정
        table.setItem(i, 0, idx)
        # 감사 제목 데이터 프레임의 i번째 행 1번째 열(감사한일) 내용을 추출
        content = QTableWidgetItem(thanks_list.iloc[i, 1])
        # 추출한 감사한일을 테이블의 i번째 행 1번째 열로 설정
        table.setItem(i, 1, content)
        # 감사 제목 데이터 프레임의 i번째 행 2번째 열(작성시간) 내용을 추출
        written_at = QTableWidgetItem(thanks_list.iloc[i, 2])
        # 추출된 작성시간을 i행 2열로 설정
        table.setItem(i, 2, written_at)

# QMainWindow 클래스를 상속받는 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    # 클래스 생성자 정의
    def __init__(self):
        # QMainWindow(상위) 클래스 생성자 호출
        super().__init__()
        # 메인 윈도우 타이틀 설정
        self.setWindowTitle("감사일기")
        # 메인 윈도우 크기 설정
        self.resize(600, 500)

        # 현재 상태의 감사 제목 데이터 프레임 추출
        thanks_list = read_data()
        # (감사 제목 데이터 프레임 행의 수) × 3 크기의 테이블을 가진 QTableWidget(테이블) 객체를 생성
        self.table = QTableWidget(len(thanks_list), 3, self)
        # 테이블의 너비가 테이블 내용에 따라 조정되도록 설정
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 테이블의 수직 헤더가 보이지 않도록 설정
        self.table.verticalHeader().setVisible(False)
        # 테이블의 칼럼명 설정
        self.table.setHorizontalHeaderLabels(['번호', '감사한일', '작성시간'])
        # 테이블 내용을 직접 수정할 수 없게 변경
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 테이블 내용 우클릭 시 메뉴가 표시되도록 설정
        self.table.setContextMenuPolicy(Qt.ActionsContextMenu)
        # 테이블에서 "수정" 메뉴 생성
        action1 = QAction("수정", self.table)
        # 테이블에서 "삭제" 메뉴 생성
        action2 = QAction("삭제", self.table)

        # 테이블 우클릭 시 수정 메뉴가 표시되도록 추가
        self.table.addAction(action1)
        # 테이블 우클릭 시 삭제 메뉴가 표시되도록 추가
        self.table.addAction(action2)
        # 데이터 프레임을 UI 테이블에 출력
        show_data(thanks_list, self.table)

        # 새로운 감사한일 입력란 QLineEdit(에딧 영역) 객체 생성
        self.input_text = QLineEdit()
        # 입력 QPushButton(버튼) 객체 생성
        self.input_btn = QPushButton("입력")
        # 입력 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.input_btn.clicked.connect(self.input_btn_clicked)

        # QHBoxLayout(상자형 수평 레이아웃) 객체를 하단 레이아웃으로 생성
        bottom_layout = QHBoxLayout()
        # 하단 레이아웃에 새로운 감사한일 입력란 추가
        bottom_layout.addWidget(self.input_text)
        # 하단 레이아웃에 입력 버튼 추가
        bottom_layout.addWidget(self.input_btn)

        # QVBoxLayout(상자형 수직 레이아웃) 객체를 전체 레이아웃으로 생성
        layout = QVBoxLayout()
        # 전체 레이아웃에 테이블 추가
        layout.addWidget(self.table)
        # 전체 레이아웃에 하단 레이아웃 추가
        layout.addLayout(bottom_layout)

        # QWidget(위젯) 객체 추가
        widget = QWidget()
        # 위젯 객체 레이아웃을 전체 레이아웃으로 설정
        widget.setLayout(layout)
        # 위젯 객체를 윈도우 중앙에 오도록 설정
        self.setCentralWidget(widget)

    # 입력 버튼 슬롯 함수 정의
    def input_btn_clicked(self):
        # 새로운 감사한일 입력란의 텍스트 추출
        new_thanks = self.input_text.text()

        # 감사한일 입력란에 유효한 텍스트가 존재한다면
        if new_thanks != '':
            # thanks.db(감사 제목 DB) sqlite3 데이터베이스를 연동하여 con으로 저장
            with sqlite3.connect("thanks.db") as con:
                # 데이터베이스 커서 객체 생성
                cur = con.cursor()
                # 감사 제목 DB에 새로운 행으로 감사한일 텍스트를 추가
                cur.execute('''
                INSERT INTO thanks_list (content) VALUES (?)
                ''', (new_thanks, ))
                # 데이터베이스 변경 내용 커밋
                con.commit()
            
            # 새로운 데이터가 추가된 데이터베이스의 내용을 추출
            thanks_list = read_data()
            # 추출한 데이터베이스의 내용을 테이블에 출력
            show_data(thanks_list, self.table)
        # 감사한일 입력란 내용을 공백으로 초기화
        self.input_text.setText('')

# 현재 코드가 메인으로 실행된 코드라면
if __name__ == '__main__':
    # QApplication 객체 생성
    app = QApplication(sys.argv)
    # 메인 윈도우 객체 생성
    w = MainWindow()
    # 메인 윈도우 출력
    w.show()
    # QApplication 실행
    app.exec()