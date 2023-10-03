# 사용자 입력 받아 TTS 실행하는 프로그램

from gtts import gTTS
from playsound import playsound
import os

# 한국어가 포함되었는지 체크하여 TTS 언어를 설정하는 함수
def check_language(text):
    # 한글 유니코드 범위 44032~55203
    korean_range = (44032, 55203)

    # 텍스트의 모든 문자에 대하여 검사
    for char in text:
        # 문자의 유니코드 추출
        char_code = ord(char)
        # 문자 유니코드 중 한글 유니코드가 발견되면(44032와 55203 사이의 유니코드가 감지되면)
        if korean_range[0] <= char_code <= korean_range[1]:
            # 언어 설정을 한국어로 설정
            return 'ko'
    # 텍스트에 한글 유니코드가 감지되지 않았으면 언어 설정을 영어로 설정  
    return 'en'

# 프로그램 실행 루프
while True:
    print("TTS 음성 출력 프로그램")
    # 사용자 입력
    text_input = input("음성으로 출력할 텍스트를 입력하세요. 아무것도 입력하지 않으면 종료됩니다.\n >> ")
    # 아무것도 입력하지 않으면 종료
    if text_input == "":
        break
    # 입력받은 텍스트의 언어 체크
    tts_lang = check_language(text_input)
    # 텍스트를 언어에 맞는 TTS로 변경
    tts = gTTS(text_input, lang=tts_lang)
    # TTS를 임시 사운드 파일로 저장
    tts.save('sound.mp3')
    # 임시 사운드 파일 재생
    playsound('sound.mp3')
    # 임시 사운드 파일 제거
    os.remove('sound.mp3')
    print("\n")

# 프로그램 종료
print("프로그램을 종료합니다.")