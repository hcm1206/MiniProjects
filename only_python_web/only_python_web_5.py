# 액셀 파일 업로드 및 업로드한 파일을 그래프로 시각화하는 기능 추가

import streamlit as st
import pandas as pd

# 웹 페이지에 작성한 마크다운 렌더링
st.write("""
# 데이터 시각화
전달 받은 액셀 파일을 시각화해줍니다.
""")

# 사용자가 파일 업로드는 요소 생성
uploaded_file = st.file_uploader("Choose a file")
# 업로드된 파일이 존재한다면
if uploaded_file is not None:
    # 사용자가 업로드한 액셀 파일 로드하여 데이터 프레임으로 저장
    df = pd.read_excel(uploaded_file)
    # 데이터 프레임에서의 연도 칼럼을 인덱스로 설정
    df = df.set_index('연도')
    # 데이터 프레임 내용을 표로 웹 페이지에 렌더링
    st.write(df)
    # 데이터 프레임 내용을 막대 그래프로 웹 페이지에 렌더링
    st.bar_chart(df)