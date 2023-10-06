# 인증된 자신 번호에게 보내는 twilio 무료 계정용 SMS 전송

from twilio.rest import Client

# twilio 계정 SID, 인증 토큰 설정
account_sid = '*검열됨*'
auth_token = '*검열됨*'
# SID와 인증 토큰을 통해 twilio 요청 클라이언트 객체 생성
client = Client(account_sid, auth_token)

# twilio 클라이언트 객체를 통해 SMS 전송
message = client.messages \
                .create(
                    # SMS 내용
                     body="twilio 문자 메시지 전송 테스트입니다.",
                     # twilio 송신 번호
                     from_='*검열됨*',
                     # 수신 번호
                     to='*검열됨*'
                 )

# SMS의 SID 출력
print(message.sid)