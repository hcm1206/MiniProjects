from html2image import Html2Image

# Html2Image 객체 생성
html = Html2Image()
# html 소스
html_src = '''
    <div>
        <div id="top"></div>
        <div id="bottom"></div>
    /div>
'''
# css 소스
css_src = '''
    #top {width: 1000px; height: 300px; background-color: #0058b5;}
    #bottom {width: 1000px; height: 300px; background-color: #f7ce00;}
'''

# html 소스와 css 소스를 토대로 구현된 웹페이지 화면 캡처해서 이미지 파일로 저장
html.screenshot(html_str = html_src, css_str = css_src, save_as = "ukraine.png")