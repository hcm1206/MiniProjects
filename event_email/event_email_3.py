# 이메일 내용에 HTML 형식 적용

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 네이버 SMTP 서버명 및 포트 설정
smtp_server = 'smtp.naver.com'
smtp_port = 587

# 네이버 SMTP 서버와 포트에 연결하는 SMTP 객체 생성
s = smtplib.SMTP(smtp_server, smtp_port)
# TLS 보안 실시
s.starttls()

# 발신 이메일 주소 및 비밀번호
email = '느그@naver.com'
email_pw = '느그비밀번호'

# 발신 이메일에 로그인
s.login(email, email_pw)

# 수신 이메일 주소
recv_email = "우리@gmail.com"
# 이메일 제목
subject = "입영통지서"
# 이메일 내용(HTML 형식 적용)
text = '''
<p style="color: olive; font-size: 20px;">입영통지서</p>
<p>당신은 <span style="background-color: red; color: white;">입영대상자</span>입니다.</p>
<p><span style="font-style: italic;">첨부된 통지서</span>를 확인하시오.</p> 
'''

# MIMEMultipart 객체 생성
msg = MIMEMultipart()
# MIMEText 객체 생성하여 이메일 내용 텍스트를 HTML 형식으로 저장
msg_text = MIMEText(text, 'html')
# MINEMultipart 객체에 MIMEText 객체(텍스트) 추가
msg.attach(msg_text)

# 텍스트 파일 로드
with open('./입영통지서.txt', 'rb') as f:
    # 텍스트 파일을 읽기 모드로 추가하여 MIMEApplication 객체 생성
    msg_file = MIMEApplication(f.read())
    # 첨부파일 헤더 추가
    msg_file.add_header('Content-Disposition', 'attachment', filename="입영통지서.txt")
    # MIMEMultipart 객체에 첨부파일 객체 추가
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