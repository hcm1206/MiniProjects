# QR코드 생성 프로그램

import qrcode

# QR코드로 접근할 URL 설정
url = "https://youtu.be/D1r9_zdygpw?si=f5laTJYL1XU8z6pS"
# QR코드 이미지 생성
qrcode_img = qrcode.make(url)
# 생성한 QR코드 이미지 png 파일로 저장
qrcode_img.save('./music_now_qrcode.png')