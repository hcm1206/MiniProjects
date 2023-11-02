# POST 요청으로 왕 추가 시 이미 존재하는 왕 순번일 경우 오류 처리

from flask import Flask, jsonify, make_response, request

# Flask 서버 객체 생성
app = Flask(__name__)
# Flask에서 JSON의 정보를 ASCII로 인식하지 않도록 설정 (Flask 2.3버전 이상)
app.json.ensure_ascii = False

# 조선시대 왕 정보를 딕셔너리 형태로 저장
kings = {
    "1": "태조", "2": "정종", "3": "태종", "4": "세종", "5": "문종", "6": "단종",
    "7": "세조", "8": "예종", "9": "성종", "10": "연산군", "11": "중종", "12": "인종",
    "13": "명종", "14": "선조", "15": "광해군", "16": "인조", "17": "효종", "18": "현종",
    "19": "숙종", "20": "경종", "21": "영조", "22": "정조", "23": "순조", "24": "헌종",
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

# /kings/<nth> 주소로 접속하여 POST 요청 시
@app.route("/kings/<nth>", methods=["POST"])
# add_king() 함수에 주소로 입력된 nth 값을 입력하여 실행
def add_king(nth):
    # request(요청) 객체를 json 형태로 생성 
    req = request.get_json()
    # 입력받은 nth가 왕 정보의 Key(순번)에 포함되어 있지 않다면
    if nth not in list(kings.keys()):
        # 왕 정보 딕셔너리에 입력된 nth를 Key로, request에서 요청받은 'name' 변수를 Value으로 하여 데이터 추가
        kings[nth] = req['name']
        # request 처리 후 왕이 생성되었다는 메시지를 json 형식으로 200(성공) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"message": "왕이 생성되었습니다."}), 200)
    # 입력받은 nth가 왕 정보의 Key(순번)와 중복되는 값이라면
    else:
        # 이미 존재하는 왕의 정보라는 오류 메시지를 json 형식으로 400(실패) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"error": "이미 존재하는 왕의 번호가 전달되었습니다."}), 400)
    return res

# 현재 코드가 메인으로 실행된 코드라면
if __name__ == '__main__':
    # 5000포트 주소로 서버 접속을 허용하여 Flask 서버 실행
    app.run(host="0.0.0.0", port=5000, debug=True)