# ACCESS TOKEN 발급 시에만 API 사용할 수 있도록 설정

from flask import Flask, jsonify, make_response, request, abort
from functools import wraps

# Flask 서버 객체 생성
app = Flask(__name__)
# Flask에서 JSON의 정보를 ASCII로 인식하지 않도록 설정 (Flask 2.3버전 이상)
app.json.ensure_ascii = False

# 임의의 ACCESS_TOKEN 설정
ACCESS_TOKEN = 'q1w2e3r4!'

# 조선시대 왕 정보를 딕셔너리 형태로 저장
kings = {
    "1": "태조", "2": "정종", "3": "태종", "4": "세종", "5": "문종", "6": "단종",
    "7": "세조", "8": "예종", "9": "성종", "10": "연산군", "11": "중종", "12": "인종",
    "13": "명종", "14": "선종", "15": "광해군", "16": "인조", "17": "효종", "18": "현종",
    "19": "숙종", "20": "경종", "21": "영조", "22": "정조", "23": "순조", "24": "현종",
    "25": "철종", "26": "고종",
}

# 액세스 토큰 인증 함수 정의
def access_token_required(func):
    # wrapper 함수가 래핑한 func 함수에 대한 메타데이터 유지
    @wraps(func)
    # func 함수 실행하기 전 실행할 wrapper 함수 정의
    def wrapper(*args, **kwargs):
        # request 요청 시 Authorization 변수에서 "Bearer (액세스 토큰)"을 추출하여 입력된 액세스 토큰과 서버에서 정의된 액세스 토큰이 같다면
        if request.headers.get('Authorization').split(' ')[1] == ACCESS_TOKEN:
            # 래핑한 func 함수 실행
            return func(*args, **kwargs)
        # 액세스 토큰이 일치하지 않다면
        else:
            # 401(인증 실패) 코드를 전송하며 요청 취소
            abort(401)
    # wrapper 함수 반환
    return wrapper

# 루트 주소(/)로 접속 시
@app.route("/")
# hello_world() 함수 실행해서 HTML로 서비스 설명글 출력
def hello_world():
    return "<p>조선시대 왕 이름 API 서비스</p>"

# /kings 주소로 접속하여 GET 요청 시
@app.route("/kings", methods=["GET"])
# 액세스 토큰 필요
@access_token_required
# get_kings() 함수 실행하여 조선시대 왕 정보를 json 형식으로 200(성공) 코드와 함께 전송하여 응답
def get_kings():
    res = make_response(jsonify(kings), 200)
    return res

# /kings/<nth> 주소로 접속하여 POST 요청 시
@app.route("/kings/<nth>", methods=["POST"])
# 액세스 토큰 필요
@access_token_required
# add_king() 함수에 주소로 입력된 nth 값을 입력하여 실행
def add_king(nth):
    # request(요청) 객체를 json 형태로 생성
    req = request.get_json()

    # 입력받은 nth가 왕 정보의 Key(순번)에 포함되어 있지 않다면
    if nth not in list(kings.keys()):
        # 왕 정보 딕셔너리에 입력된 nth를 Key로, request에서 요청받은 'name' 변수를 Value로 하여 데이터 추가
        kings[nth] = req['name']
        # request 처리 후 왕이 생성되었다는 메시지를 json 형식으로 200(성공) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"message": "왕이 생성되었습니다."}), 200)
    # 입력받은 nth가 왕 정보의 Key(순번)에 존재하지 않는 값이라면
    else:
        # 이미 존재하는 왕의 정보라는 오류 메시지를 json 형식으로 400(실패) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"error": "이미 존재하는 왕의 번호가 전달되었습니다."}), 400)
    return res

# /kings/<nth> 주소로 접속하여 PUT 요청 시
@app.route("/kings/<nth>", methods=["PUT"])
# 액세스 토큰 필요
@access_token_required
# update_king() 함수에 주소로 입력된 nth 값을 입력하여 실행
def update_king(nth):
    # request(요청) 객체를 json 형태로 생성
    req = request.get_json()
    # 생성된 request 객체 출력
    print(req)

    # 입력받은 nth가 왕 정보의 Key(순번)에 존재하는 값이라면
    if nth in list(kings.keys()):
        # 해당 Key(순번)의 왕 이름을 request에서 요청받은 'name' 변수로 변경하여 저장
        kings[nth] = req['name']
        # request 처리 후 왕이 수정되었다는 메시지를 json 형식으로 200(성공) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"message": "왕이 수정되었습니다."}), 200)
    # 입력받은 nth가 왕 정보의 Key(순번)에 존재하지 않는 값이라면
    else:
        # 없는 번호의 왕이라는 오류 메시지를 json 형식으로 400(실패) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"error": "없는 번호의 왕입니다."}), 400)
    return res

# /kings/<nth> 주소로 접속하여 DELETE 요청 시
@app.route("/kings/<nth>", methods=["DELETE"])
# 액세스 토큰 필요
@access_token_required
# delete_king() 함수에 주소로 입력된 nth 값을 입력하여 실행
def delete_king(nth):
    # 입력받은 nth가 왕 정보의 Key(순번)에 존재하는 값이라면
    if nth in list(kings.keys()):
        # 해당 Key(순번) 왕을 왕 목록 딕셔너리에서 삭제
        del kings[nth]
        # 왕이 삭제되었다는 메시지를 json 형식으로 200(성공) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"message": "왕이 삭제되었습니다."}), 200)
    # 입력받은 nth가 왕 정보의 Key(순번)에 존재하지 않는 값이라면
    else:
        # 없는 번호의 왕이라는 오류 메시지를 json 형식으로 400(실패) 코드와 함께 전송하여 응답
        res = make_response(jsonify({"error": "없는 번호의 왕입니다."}), 400)
    return res

# 현재 코드가 메인으로 실행된 코드라면
if __name__ == '__main__':
    # 5000 포트 주소로 서버 접속을 허용하여 Flask 서버 실행
    app.run(host="0.0.0.0", port=5000, debug=True)