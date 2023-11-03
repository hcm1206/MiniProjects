# 번역 사이트 서버 구현

from flask import Flask, render_template, request, jsonify, make_response
from googletrans import Translator

# Flask 서버 객체 생성
app = Flask(__name__)
# 번역기 객체 생성
simpago = Translator()

# 루트 주소(/)로 접속 시
@app.route("/")
# index() 함수를 실행하여 index.html 파일을 렌더링
def index():
    return render_template('index.html')

# /translate 주소로 POST 요청 시
@app.route("/translate", methods=['POST'])
# translate() 함수 실행
def translate():
    # 요청받은 내용을 json 형식으로 저장
    req = request.get_json()
    # 요청받은 내용 중 'trans_src' 속성을 받아서 출력
    trans_src = req['trans_src']
    print(trans_src)

    # 'trans_src' 속성을 한국어에서 영어로 번역 후 번역본 출력
    trans_dest = simpago.translate(trans_src, dest='en', src='ko')
    print(trans_dest.text)

    # 번역본을 'result'에 담아 json화하여 200(성공) 코드와 함께 전송하여 응답
    res = make_response(jsonify({'result': trans_dest.text}), 200)
    return res

# 현재 코드가 메인으로 실행된 코드라면
if __name__ == '__main__':
    # 5000 포트 주소로 서버 접속을 허용하여 Flask 서버 실행
    app.run(host="0.0.0.0", port=5000, debug=True)