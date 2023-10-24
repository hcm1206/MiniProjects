# 류현진의 시즌별 평균자책점 그래프를 한글 폰트 문제 수정하여 출력

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 시스템의 굴림체 폰트 경로 지정
font_path = "C:/Windows/Fonts/gulim.ttc"
# 시스템 경로를 통해 굴림체 폰트 불러옴
font = font_manager.FontProperties(fname=font_path).get_name()
# 폰트를 굴림체 폰트로 설정
rc('font', family=font)

# MLB 데이터가 포함된 레만 데이터베이스 로드
with sqlite3.connect("lahmansbaseballdb.sqlite") as con:
    # 커서 객체 생성
    cur = con.cursor()
    # SQL문 (투구 테이블에서 류현진의 정보 (선수ID, 연도, 팀, 승, 패, 경기수, 세이브, 아웃카운트, 평균자책점, 탈삼진, 볼넷, 피안타) 조회) 실행
    cur.execute('''
    SELECT playerID, yearID, teamID, W, L, G, SV, IPouts, ERA, SO, BB, H
    FROM pitching WHERE playerID = 'ryuhy01';
    ''')
    # 조회 결과 저장
    result = cur.fetchall()

# 컬럼명을 담을 빈 리스트 생성
cols = []
# 커서의 각 열 별로 반복
for column in cur.description:
    # 각 열의 정보(컬럼명)를 리스트에 저장
    cols.append(column[0])

# 조회 결과를 컬럼 리스트에 맞게 데이터 프레임 형태로 저장
df = pd.DataFrame.from_records(data=result, columns=cols)
# 데이터 프레임 출력
print(df)

# x축을 각 시즌, y축을 평균자책점으로 하는 그래프 생성
plt.plot(df['yearID'], df['ERA'])
# 그래프 제목 설정
plt.title('류현진 시즌별 ERA 추이')
# x축 제목 설정
plt.xlabel('시즌')
# y축 제목 설정
plt.ylabel('ERA')
# 그래프 격자 표시 설정
plt.grid(True)
# 그래프 출력
plt.show()