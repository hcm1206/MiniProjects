from html2image import Html2Image

# Html2Image 객체 생성
html = Html2Image()
# 여러 페이지들을 각각 캡처한 이미지 파일들에 이름을 붙여 한 번에 생성
html.screenshot(url=["https://www.google.com/", "https://www.youtube.com/", "https://github.com/"],
                save_as=["google.png", "youtube.png", "github.png"])
