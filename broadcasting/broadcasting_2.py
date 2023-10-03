# 영어 TTS

from gtts import gTTS

# 텍스트 설정
text = "We are studying Python right now."
# 텍스트를 영어 TTS로 변환
tts = gTTS(text, lang='en')
# 영어 TTS를 mp3 파일로 저장
tts.save('result1.mp3')