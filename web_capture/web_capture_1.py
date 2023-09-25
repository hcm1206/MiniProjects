from html2image import Html2Image

# Html2Image 객체 생성
html = Html2Image()
# 해당 유튜브 링크 페이지를 캡처하여 이미지 파일로 저장
html.screenshot(url="https://youtu.be/A_MjCqQoLLA?si=1t5UMHH1u-pHD9HW", save_as="listeningNow.png")