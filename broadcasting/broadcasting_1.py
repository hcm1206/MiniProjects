# 한국어 TTS

from gtts import gTTS

# 텍스트 설정
text = "저희는 지금 파이썬을 공부하고 있습니다."
# 텍스트를 한국어 TTS로 변환
tts = gTTS(text, lang='ko')
# 한국어 TTS를 mp3 파일로 저장
tts.save('result.mp3')