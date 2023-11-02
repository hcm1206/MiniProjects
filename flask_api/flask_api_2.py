# Flask 서버로 조선시대 왕 API 구현

from flask import Flask, jsonify, make_response
import json

# Flask 서버 객체 생성
app = Flask(__name__)

# Flask에서 JSON의 정보를 ASCII로 인식하지 않도록 설정 (Flask 2.3버전 미만)
# app.config['JSON_AS_ASCII'] = False

# Flask에서 JSON의 정보를 ASCII로 인식하지 않도록 설정 (Flask 2.3버전 이상)
app.json.ensure_ascii = False

# 조선시대 왕 정보를 딕셔너리 형태로 저장
kings = {
    "1": "태조", "2": "정종", "3": "태종", "4": "세종", "5": "문종", "6": "단종", 
    "7": "세조", "8": "예종", "9": "성종", "10": "연산군", "11": "중종", "12": "인종",
    "13": "명종", "14": "선조", "15": "광해군", "16": "인조", "17": "효종", "18": "현종", 
    "19": "숙종", "20": "경종", "21": "영조", "22": "정조", "23": "순조", "24": "현종",
    "25": "철종", "26": "고종",
}

# 루트 주소(/)로 접속 시
@app.route("/")
# hello_world() 함수 실행하여 HTML로 서비스 설명글 출력
def hello_world():
    return "<p>조선시대 왕 이름 API 서비스</p>"

# /kings 주소로 접속하여 GET 요청 시
@app.route("/kings", methods=["GET"])
# get_kings() 함수 실행하여 조선시대 왕 정보를 json 형식으로 200(성공) 코드와 함께 전송하여 응답
def get_kings():
    res = make_response(jsonify(kings), 200)
    return res

# 현재 코드가 메인으로 실행된 코드라면 
if __name__ == '__main__':
    # 5000포트 주소로 서버 접속을 허용하여 Flask 서버 실행
    app.run(host="0.0.0.0", port=5000, debug=True)