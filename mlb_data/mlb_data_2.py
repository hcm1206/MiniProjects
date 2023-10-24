# 류현진 투구 데이터를 데이터 프레임으로 출력

import sqlite3
import pandas as pd

# MLB 데이터가 포함된 레먼 데이터베이스 로드
with sqlite3.connect("lahmansbaseballdb.sqlite") as con:
    # 커서 객체 생성
    cur = con.cursor()
    # SQL문 (투구 테이블에서 류현진의 정보(선수ID, 연도, 팀, 승, 패, 경기수, 세이브, 아웃카운트, 평균자책점, 탈삼진, 볼넷, 피안타) 조회) 실행
    cur.execute('''
    SELECT playerID, yearID, teamID, W, L, G, SV, IPouts, ERA, SO, BB, H
    FROM pitching WHERE playerID = 'ryuhy01';
    ''')
    # 조회 결과 저장
    result = cur.fetchall()

# 컬럼명을 담을 빈 리스트 생성
cols = []
# 커서의 열 별로 반복
for column in cur.description:
    # 각 열의 정보(컬럼명)를 리스트에 저장
    cols.append(column[0])

# 조회 결과를 컬럼 리스트에 맞게 데이터 프레임 형태로 저장
df = pd.DataFrame.from_records(data=result, columns=cols)
# 데이터 프레임 출력
print(df)