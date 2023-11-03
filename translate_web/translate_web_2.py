# googletrans 라이브러리가 지원하는 번역 가능한 언어 목록 출력

import googletrans

# googletrans 라이브러리가 지원하는 번역 가능한 언어 목록 출력
print(f"지원하는 언어 목록 : {googletrans.LANGUAGES}")

# googletrans 라이브러리가 지원하는 번역 가능한 언어 개수 출력
print(f"지원하는 언어 개수 : {len(googletrans.LANGUAGES)}")