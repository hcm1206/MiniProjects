# 감사 제목 DB 내용을 GUI 창으로 출력

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, QAbstractItemView
import sqlite3
import pandas as pd

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

        # thanks.db(감사 제목 DB) sqlite3 데이터베이스를 연동하여 con으로 저장
        with sqlite3.connect("thanks.db") as con:
            # 데이터베이스 커서 객체 생성
            cur = con.cursor()
            # 감사 제목 DB의 인덱스, 내용, 생성 날짜 조회 쿼리문 실행
            cur.execute('''
                SELECT idx, content, created_at FROM thanks_list;
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

        # (감사 제목 데이터 프레임 행의 수) × 3 크기의 테이블을 가진 QTableWidget(테이블) 객체를 생성
        self.table = QTableWidget(len(thanks_list), 3, self)
        # 테이블의 너비가 테이블 내용에 따라 조정되도록 설정
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 테이블의 수직 헤더가 보이지 않도록 설정
        self.table.verticalHeader().setVisible(False)
        # 테이블의 컬럼명 설정
        self.table.setHorizontalHeaderLabels(['번호', '감사한일', '작성시간'])
        # 테이블 내용을 직접 수정할 수 없게 설정
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 반복 변수 i를 이용하여 감사 제목 데이터 프레임의 내용(행)마다 반복
        for i in range(len(thanks_list)):
            # 감사 제목 데이터 프레임의 i번째 행 0번째 열(번호) 내용을 문자열로 추출
            idx = QTableWidgetItem(str(thanks_list.iloc[i, 0]))
            # 추출된 번호를 테이블의 i행 0열 내용으로 설정
            self.table.setItem(i, 0, idx)
            # 감사 제목 데이터 프레임의 i번째 행 1번째 열(감사한일) 내용을 추출
            content = QTableWidgetItem(thanks_list.iloc[i, 1])
            # 추출된 감사한일을 테이블의 i행 1열 내용으로 설정
            self.table.setItem(i, 1, content)
            # 감사 제목 데이터 프레임의 i번째 행 2번째 열(작성시간)으로 설정
            written_at = QTableWidgetItem(thanks_list.iloc[i, 2])
            # 추출된 작성시간을 테이블의 i행 2열 내용으로 설정
            self.table.setItem(i, 2, written_at)

        # QVBoxLayout(상자형 수직 레이아웃) 객체를 전체 레이아웃으로 생성
        layout = QVBoxLayout()
        # 전체 레이아웃에 테이블 추가
        layout.addWidget(self.table)

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
    w = MainWindow()
    # 메인 윈도우 출력
    w.show()
    # QApplication 실행
    app.exec()
