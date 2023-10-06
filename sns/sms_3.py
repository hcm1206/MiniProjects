# 특정 형식으로 작성된 액셀 파일의 모든 전화번호로 SMS 전송

from twilio.rest import Client
import pandas as pd

# twilio 계정 SID, 인증 토큰 설정
account_sid = '*검열됨*'
auth_token = '*검열됨*'
# SID와 인증 토큰을 이용해 twilio 요청 클라이언트 객체 생성
client = Client(account_sid, auth_token)

# 회원정보 액셀 파일 로드
df = pd.read_excel('./회원정보.xlsx')
# 액셀 파일의 정보 출력
print(df, "\n")

# 액셀의 각 행 별로 반복
for idx, row in df.iterrows():
    try:
        # 액셀 형식에서 전화번호를 추출하여 하이픈(-) 제거
        phone_num = row['전화번호'].replace("-", "")
        # twilio 클라이언트 객체를 통해 SMS 전송
        message = client.messages \
                            .create(
                                # SMS 내용
                                body=f'''안녕하십니까. {row['이름']} 회원님. 최강빠따 감독 김성근입니다.
                                20xx년 yy월 zz일 토요일 오후 2시에 빠따 경기가 있을 예정이오니, 모두들 참석해주기 바랍니다.''',
                                # twilio 송신 번호
                                from_='+*검열됨*',
                                # 수신 번호(추출한 전화번호)
                                to_= '+82' + phone_num
                            )
        # SMS의 status(상태) 출력
        print(message.status)
    # 예외 발생 시 예외 메시지 출력
    except Exception as e:
        print(e)