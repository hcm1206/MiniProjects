# 레먼 MLB 데이터베이스에서 류현진 투구 데이터 추출

import sqlite3

# MLB 데이터가 포함된 레먼 데이터베이스 파일 로드
with sqlite3.connect("lahmansbaseballdb.sqlite") as con:
    # 커서 객체 생성
    cur = con.cursor()
    # SQL문(투구 테이블에서 류현진의 데이터 전부 조회) 실행
    cur.execute('''
    SELECT * FROM pitching WHERE playerID = 'ryuhy01';
    ''')
    # 조회 결과를 저장
    result = cur.fetchall()

# 조회 결과 출력
print(result)