# 이메일로 임시 비밀번호 전송

import string
import random
import smtplib
from email.mime.text import MIMEText

# 임시 비밀번호 생성 함수
def make_temp_password():
    # 임시 비밀번호 저장할 문자열
    new_pw = ""

    # 영문자 중 랜덤으로 5개 뽑아 임시 비밀번호에 추가
    for i in range(5):
        new_pw += random.choice(string.ascii_letters)

    # 숫자 중 랜덤으로 3개 뽑아 임시 비밀번호에 추가
    for i in range(3):
        new_pw += random.choice(string.digits)
    
    # 특수문자 중 랜덤으로 2개 뽑아 임시 비밀번호에 추가
    for i in range(2):
        new_pw += random.choice("!@#$%^&*")

    # 임시 비밀번호의 문자열을 섞어서 완성하고 완성된 임시 비밀번호 리턴
    new_pw_shuffle = "".join(random.sample(new_pw, len(new_pw)))
    return new_pw_shuffle

# 이메일 발신 클래스 정의
class EmailSender:
    # 네이버 SMTP 주소 설정
    __smtp_server = "smtp.naver.com"
    # 네이버 SMTP 포트 설정
    __smtp_port = 587

    # 클래스 생성자(발신 이메일과 발신 이메일 비밀번호 설정)
    def __init__(self, email, email_pw):
        self.email = email
        self.email_pw = email_pw

    # 수신 이메일 설정하여 이메일 전송하는 메서드
    def send_email(self, recv_email):
        # 네이버 SMTP 서버에 연결하는 SMTP 객체 생성
        s = smtplib.SMTP(EmailSender.__smtp_server, EmailSender.__smtp_port)
        # TLS 보안 설정
        s.starttls()
        
        # 설정해둔 발신 이메일에 로그인
        s.login(self.email, self.email_pw)

        # 이메일 제목과 내용(임시 비밀번호) 설정
        subject = "임시 비밀번호 발송"
        text = f"임시 비밀번호: {make_temp_password()}"

        # 텍스트 이메일 객체 생성하여 내용(임시 비밀번호) 입력
        msg = MIMEText(text)
        # 이메일 발신자 설정
        msg['From'] = self.email
        # 이메일 수신자 설정
        msg['To'] = recv_email
        # 이메일 제목 설정
        msg['Subject'] = subject

        # 설정해둔 발신 이메일로부터 수신 이메일로 이메일 전달
        s.sendmail(self.email, recv_email, msg.as_string())
        # 이메일 전송 세션 종료
        s.quit()

# 이메일 발신 객체 생성
email_sender = EmailSender('느그@naver.com', '느그비밀번호') # 실제 발신할 이메일 주소와 암호 작성
# 이메일 발신 객체에서 임시 비밀번호 생성하여 이메일 전송
email_sender.send_email('우리@gmail.com') # 실제 수신할 이메일 주소와 암호 작성


    