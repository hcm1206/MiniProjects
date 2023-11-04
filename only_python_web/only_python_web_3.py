# 웹에 렌더링된 그래프 인덱스 설정 변경

import streamlit as st
import pandas as pd

# 웹 페이지에 작성한 마크다운 렌더링
st.write("""
# 1014번 버스 승차객수 추이
서울 1014번 버스의 연간 승차객수 추이 그래프입니다\n
2013년부터 2022년까지
""")

# 엑셀 파일 로드하여 데이터 프레임 형태로 저장
df = pd.read_excel("bus.xlsx")
# 원본 데이터 프레임 출력
print(df)

# 데이터 프레임의 연도 컬럼을 문자열 타입으로 변경
df['연도'] = df['연도'].astype('str')
# 데이터 프레임에서의 인덱스를 연도 칼럼으로 설정
df = df.set_index('연도')
# 변경한 데이터 프레임 출력
print(df)

# 변경한 데이터 프레임을 선형 그래프로 웹 페이지에 렌더링
st.line_chart(df)