# 감사제목 수정/삭제 기능 구현

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, \
    QLineEdit, QPushButton, QAbstractItemView, QLabel
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
    # 감사 제목 DB의 칼렴명들을 칼람명 리스트에 별도로 저장
    for column in cur.description:
        cols.append(column[0])
    
    # 감사 제목 DB의 내용과 칼럼명 리스트를 데이터 프레임 형식으로 저장
    thanks_list = pd.DataFrame.from_records(data=result, columns=cols)
    # 저장된 데이터 프레임 출력
    print(thanks_list)
    
    # 데이터 프레임 리턴
    return thanks_list

# 데이터 프레임 내용르 UI 테이블에 출력하는 함수
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
        # 추출한 감사한일을 테이블의 i번째 행 0번째 열로 설정
        table.setItem(i, 1, content)
        # 감사 제목 데이터 프레임의 i번째 행 2번째 열(작성시간) 내용을 추출
        written_at = QTableWidgetItem(thanks_list.iloc[i, 2])
        # 추출된 작성시간을 i행 2열로 설정
        table.setItem(i, 2, written_at)

# QWidget 클래스를 상속받는 ModifyWindow(수정 윈도우) 클래스 정의
class ModifyWindow(QWidget):
    # 클래스 생성자 정의(수정 전 원본 감사 제목 텍스트, 수정할 감사 제목의 인덱스, UI 테이블 객체 입력받음)
    def __init__(self, current_item_text, current_item_idx, table):
        # QWidget(상위) 클래스 생성자 호출
        super().__init__()
        # 수정 윈도우 타이틀 설정
        self.setWindowTitle("감사내용 수정")
        # 수정 윈도우 너비 설정
        self.setFixedWidth(600)
        # 수정할 감사 제목의 인덱스를 맴버변수로 저장
        self.update_idx = current_item_idx
        # 수정할 UI 테이블 객체를 맴버변수로 저장
        self.table = table
        
        # 수정 전 원본 감사 제목 QLabel(라벨) 객체 생성
        self.lb = QLabel(current_item_text)
        # 수정할 감사 제목 입력란 QLineEdit(에딧 영역) 객체 생성
        self.qle = QLineEdit()
        # 수정 QPushButton(버튼) 객체 생성
        self.btn = QPushButton("수정")
        # 수정 버튼 클릭(시그널) 시 실행할 함수(슬롯) 설정
        self.btn.clicked.connect(self.modify_btn_clicked)

        # QVBoxLayout(상자형 수직 레이아웃) 객체를 수정 윈도우 전체 레이아웃으로 생성
        layout = QVBoxLayout()
        # 수정 윈도우 전체 레이아웃에 수정 전 원본 감사 제목 라벨 추가
        layout.addWidget(self.lb)
        # 수정 윈도우 전체 레이아웃에 수정할 감사 제목 입력란 추가
        layout.addWidget(self.qle)
        # 수정 윈도우 전체 레이아웃에 수정 버튼 추가
        layout.addWidget(self.btn)
        # 자기 자신 QWidget(위젯) 객체의 레이아웃을 수정 윈도우 전체 레이아웃으로 설정
        self.setLayout(layout)

    # 수정 버튼 슬롯 함수 정의
    def modify_btn_clicked(self):
        # 수정할 감사 제목 입력란의 텍스트를 추출
        update_thanks = self.qle.text()
        # 수정할 감사 제목의 인덱스를 추출
        update_idx = self.update_idx

        # 수정할 감사 제목 입력란에 유효한 텍스트가 존재한다면
        if update_thanks:
            # thanks.db(감사 제목 DB) sqlite3 데이터베이스를 연동하여 con으로 저장
            with sqlite3.connect("thanks.db") as con:
                # 데이터베이스 커서 객체 생성
                cur = con.cursor()
                # 감사 제목 DB에서 해당하는 인덱스의 감사 제목 내용을 입력된 감사 제목으로 변경
                cur.execute('''
                UPDATE thanks_list SET content = (?) WHERE idx = (?);
                ''', (update_thanks, update_idx))
                # 데이터베이스에 추가한 내용 커밋
                con.commit()
            
            # 데이터가 갱신된 데이터베이스의 내용을 추출
            thanks_list = read_data()
            # 추출한 데이터베이스의 내용을 테이블에 출력
            show_data(thanks_list, self.table)

        # 수정 완료 후 이 수정 윈도우를 종료
        self.close()

# QMainWindow를 상속받는 메인 윈도우 클래스 정의
class MainWindow(QMainWindow):
    # 클래스 생성자 정의
    def __init__(self):
        # QMainWindow(상위) 클래스 생성자 호출
        super().__init__()
        # 메인 윈도우 타이틀 설정
        self.setWindowTitle("감사일기")
        # 메인 윈도우 크기 설정
        self.resize(600, 500)

        # 현재 상태의 감사 제목 데이터프레임 추출
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

        # 테이블 우클릭 시 메뉴가 표시되도록 설정
        self.table.setContextMenuPolicy(Qt.ActionsContextMenu)
        # 테이블에서 "수정" 메뉴 생성
        action1 = QAction("수정", self.table)
        # 테이블에서 "삭제" 메뉴 생성
        action2 = QAction("삭제", self.table)
        # 수정 메뉴 클릭 시 modify(수정) 함수가 실행되도록 연결
        action1.triggered.connect(self.modify)
        # 삭제 메뉴 클릭 시 delete(삭제) 함수가 실행되도록 연결
        action2.triggered.connect(self.delete)
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

        # QBoxLayout(상자형 수평 레이아웃) 객체를 하단 레이아웃으로 생성
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
                # 감사 제목 DB에 새로운 행으로 감사한일 텍스트 추가
                cur.execute('''
                INSERT INTO thanks_list (content) VALUES (?);
                ''', (new_thanks, ))
                # 데이터베이스 변경 내용 커밋
                con.commit()

            # 새로운 데이터가 추가된 데이터베이스의 내용을 추출
            thanks_list = read_data()
            # 추출한 데이터베이스의 내용을 테이블에 출력
            show_data(thanks_list, self.table)
        # 감사한일 입력한 내용을 공백으로 초기화
        self.input_text.setText('')

    # 수정 메뉴 선택 시 실행되는 수정 함수 정의
    def modify(self):
        # 테이블에서 선택된 데이터 추출
        current_item = self.table.currentItem()
        # 선택된 데이터의 행 추출
        current_item_row = current_item.row()
        # 선택된 데이터의 행에서 감사한일 내용 추출
        current_item_text = self.table.item(current_item_row, 1).text()
        # 선택된 데이터의 행에서 번호를 텍스트로 추출
        current_item_idx = int(self.table.item(current_item_row, 0).text())
        # 선택된 감사한일 내용과 해당 인덱스, 테이블을 입력하여 수정 윈도우 객체 생성
        self.modify_window = ModifyWindow(current_item_text, current_item_idx, self.table)
        # 수정 윈도우 출력
        self.modify_window.show()

    # 삭제 메뉴 선택 시 실행되는 삭제 함수 정의
    def delete(self):
        # 테이블에서 선택된 데이터 추출
        current_item = self.table.currentItem()
        # 선택된 데이터의 행 추출
        current_item_row = current_item.row()
        # 선택된 데이터의 행에서 번호를 텍스트로 추출
        current_item_idx = int(self.table.item(current_item_row, 0).text())

        # thanks.db(감사 제목 DB) sqlite3 데이터베이스를 연동하여 con으로 저장
        with sqlite3.connect("thanks.db") as con:
            # 데이터베이스 커서 객체 생성
            cur = con.cursor()
            # 감사 제목 DB에서 추출된 인덱스의 행을 테이블에서 제거
            cur.execute('''
            DELETE FROM thanks_list WHERE idx = (?);
            ''', (current_item_idx, ))
            # 데이터베이스 변경 내용 커밋
            con.commit()

        # 데이터가 삭제된 데이터베이스의 내용을 추출
        thanks_list = read_data()
        # 추출한 데이터베이스의 내용을 테이블에 출력
        show_data(thanks_list, self.table)

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