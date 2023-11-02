# Flask 서버 생성

from flask import Flask

# Flask 서버 객체 생성
app = Flask(__name__)

# 루트 주소(/)로 접속 시
@app.route("/")
# hello_world() 함수 실행하여 HTML 코드 출력
def hello_world():
    return "<p>Hello, World!</p>"

# 현재 코드가 메인으로 실행된 코드라면 
if __name__ == '__main__':
    # 5000포트 주소로 서버 접속을 허용하여 Flask 서버 실행
    app.run(host="0.0.0.0", port=5000, debug=True)