# googletrans 라이브러리를 이용해서 한국어를 영어로 번역

from googletrans import Translator

# 번역기 객체 생성
simpago = Translator()

# 번역할 원문 설정
trans_src = "저는 지금 파이썬 코딩에 관한 책을 쓰고 있습니다."
# 번역기 객체를 통해 원문을 한국어에서 영어로 번역 후 번역본 저장
trans_dest = simpago.translate(trans_src, dest='en', src='ko')

# 원문 출력
print(f"원문: {trans_src}")
# 번역본 출력
print(f"번역: {trans_dest.text}")