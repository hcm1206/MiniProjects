# 웹에 matplotlib 그래프 렌더링

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 웹 페이지에 작성한 마크다운 렌더링
st.write("""
# 1014번 버스 승차객수 추이
서울 1014번 버스의 연간 승차객수 추이 그래프입니다\n
2013년부터 2022년까지
""")

# 액셀 파일 로드하여 데이터 프레임 형태로 저장
df = pd.read_excel("bus.xlsx")
# 데이터 프레임에서의 연도 칼럼을 인덱스로 설정
df = df.set_index('연도')

# 데이터 프레임을 나타낼 그래프 객체 생성
plt.plot(df)
# 그래프의 격자를 보이게 설정
plt.grid(True)
# 그래프 x축 제목 설정
plt.xlabel('month')
# 그래프 y축 제목 설정
plt.ylabel('visit')
# 그래프 x축 간격을 데이터 프레임의 인덱스로 설정
plt.xticks(df.index)

# 생성된 그래프 객체를 웹 페이지에 렌더링
st.pyplot(plt)