# 타인 전화번호에게 보내는 twilio 유료 계정용 SMS 전송

from twilio.rest import Client

# twilio 계정 SID, 인증 토큰 설정
account_sid = '*검열됨*'
auth_token = '*검열됨*'
# SID와 인증 토큰을 이용해 twilio 요청 클라이언트 객체 생성
client = Client(account_sid, auth_token)

# twilio 클라이언트 객체를 통해 SMS 전송
message = client.messages \
                .create(
                    # SMS 내용
                    body="♚♚히어로즈 오브 더 스☆톰♚♚가입시$$전원 카드팩☜☜뒷면100%증정※ ♜월드오브 워크래프트♜펫 무료증정￥ 특정조건 §§디아블로3§§★공허의유산★초상화획득기회@@ 즉시이동http://kr.battle.net/heroes/ko/",
                    # twilio 송신 번호
                    from_='+*검열됨*',
                    # 수신 번호
                    to_='*검열됨*' # 수신자 휴대폰 번호
                )
# SMS의 SID 출력
print(message.sid)