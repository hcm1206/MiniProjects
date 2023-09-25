from html2image import Html2Image

# Html2Image 객체 생성
html = Html2Image()
# html 소스 작성
html_src = "<div>Hello World!<div>"
# css 소스 작성
css_src = '''
    div {
        width: 1200px;
        height: 1200px;
        background-color: blue;
        color: white;
        font-size: 100px;
        text-align: center;
    }
'''

# html 소스와 css 소스를 토대로 구현된 웹페이지 화면을 캡처하여 이미지로 저장
html.screenshot(html_str=html_src, css_str=css_src, save_as="custom.png")