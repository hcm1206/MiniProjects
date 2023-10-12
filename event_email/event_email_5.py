# 액셀에 저장된 모든 이메일주소로 이메일 전송

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd

# 네이버 SMTP 서버명 및 포트 설정
smtp_server = "smtp.naver.com"
smtp_port = 587

# 발신 이메일 주소 및 비밀번호
email = "느그@naver.com'"
email_pw = '느그비밀번호'

# 네이버 SMTP 서버와 포트에 연결하는 SMTP 객체 생성
s = smtplib.SMTP(smtp_server, smtp_port)
# TLS 보안 실시
s.starttls()
# 발신 이메일에 로그인
s.login(email, email_pw)

# 액셀에서 데이터 로드
df = pd.read_excel('./신검리스트.xlsx')
# 데이터 행 중 현역판정여부 속성이 'O'인 것만 출력
df_active_duty = df[df['현역판정여부']=="O"]

# 현역판정여부 속성이 'O'인 데이터 행마다 반복
for idx, row in df_active_duty.iterrows():
    # 현재 데이터 행 중 이름 속성을 수신자 이름으로 설정
    recv_name = row['이름']
    # 현재 데이터 행 중 진짜이메일주소 속성을 수신자 이메일 주소로 설정
    recv_email = row['진짜이메일주소']

    # 이메일 제목
    subject = f"{recv_name}님 군대영장"
    # 이메일 내용
    text = f'''
    <p>안녕하십니까. {recv_name}님. 병무청입니다.</p>
    <p>귀하는 <span style="background-color: red; color: white;">현역 입영 대상</span>입니다.
    <p><span style="font-style: italic;">첨부된 통시서</span>을 <strong>반드시</strong> 확인하십시오.</p>
    '''

    # MIMEMultipart 객체 생성
    msg = MIMEMultipart()
    # MIMEText 생성하여 이메일 내용 텍스트를 html 형식으로 저장
    msg_text = MIMEText(text, 'html')
    # MIMEMultipart 객체에 이메일 내용 텍스트 객체 추가
    msg.attach(msg_text)

    # 텍스트 파일 로드
    with open('./입영통지서.txt', 'rb') as f:
        # 텍스트 파일을 읽기모드로 불러와 MIMEApplication 객체에 저장
        msg_file = MIMEApplication(f.read())
        # 텍스트 파일에 헤더 추가
        msg_file.add_header('Content-Disposition', 'attachment', filename='입영통지서.txt')
        # 텍스트 파일을 첨부파일로 하여 MIMEMultipart 객체에 추가
        msg.attach(msg_file)

    # 발신지 설정
    msg['From'] = email
    # 수신지 설정
    msg['To'] = recv_email
    # 제목 설정
    msg['Subject'] = subject

    # 발신 이메일 주소로부터 수신 이메일 주소에 메시지를 문자열 형태로 전송
    s.sendmail(email, recv_email, msg.as_string())

# 이메일 전송 세션 종료
s.quit()