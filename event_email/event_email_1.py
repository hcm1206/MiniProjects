# 이메일 전송

import smtplib
from email.mime.text import MIMEText

# 네이버 SMTP 서버명
smtp_server = "smtp.naver.com"
# 네이버 SMTP 포트
smpt_port = 587

# 네이버 SMTP 서버와 포트에 연결하는 SMTP 객체 생성
s = smtplib.SMTP(smtp_server, smpt_port)
# TLS 보안 실시
s.starttls()

# 발신 이메일 주소 및 비밀번호
email = '느그@naver.com'
email_pw = '느그비밀번호'

# 발신 이메일 계정에 로그인
s.login(email, email_pw)

# 수신 이메일 주소
recv_email = '우리@gmail.com'
# 이메일 제목
subject = '입영통지서'
# 이메일 내용
text = '''
당신은 입영대상자입니다.
'''

# MINE 텍스트 객체 생성하여 text 저장
msg = MIMEText(text)
# 발신지 설정
msg['From'] = email
# 수신지 설정
msg['To'] = recv_email
# 제목 설정
msg['Subject'] = subject

# 발신 이메일 주소로부터 발신 이메일 주소로 메시지를 문자열 형태로 메일 발송
s.sendmail(email, recv_email, msg.as_string())
# 이메일 전송 세션 종료
s.quit()
