# 영어 번역 기능 웹 애플리케이션 구현

import streamlit as st
from googletrans import Translator

# 번역기 객체 생성
translator = Translator()

# 웹 페이지에 작성한 마크다운 렌더링
st.write("""
# 번역 모델 v0.1
입력된 텍스트를 영어로 번역합니다.
""")

# 번역할 텍스트 입력 부분 렌더링
txt = st.text_area('번역할 텍스트', 
'''
안녕하세요. 반갑습니다. 파이썬 공부 재밌게 하고 계신가요?
''')

# 번역 결과 텍스트 출력 부분에 입력된 텍스트를 한국어에서 영어로 번역하여 렌더링
st.write('번역 결과:', translator.translate(txt, dest='en', stc='ko').text)