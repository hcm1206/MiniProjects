# 삼성전자우 1주 주식 매도

import yaml
import requests
import json
from datetime import datetime

# API 키와 계좌 정보 등등 설정값을 config.yaml 파일에서 로드
with open('config.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

# 설정값 불러와 변수로 저장
APP_KEY = cfg['APP_KEY']
APP_SECRET = cfg['APP_SECRET']
CANO = cfg['CANO']
ACNT_PRDT_CD = cfg['ACNT_PRDT_CD']
URL_BASE = cfg['URL_BASE']

# 액세스 토큰 발급하는 함수
def get_access_token():
    PATH = "oauth2/tokenP"
    URL = f"{URL_BASE}/{PATH}"
    headers = {"content-type": "application/json"}
    body = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    }
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    ACCESS_TOKEN = res.json()["access_token"]
    return ACCESS_TOKEN

# 해시 키 추출하는 함수
def hash_key(body):
    PATH = "uapi/hashkey"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        'content-Type': 'application/json',
        "appkey": APP_KEY,
        "appSecret": APP_SECRET,
    }    
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    hashkey = res.json()["HASH"]
    return hashkey

# 입력한 코드에 해당하는 주식을 입력된 주만큼 매도하는 함수
def sell_stock(code: str, qty: int):
    PATH = "uapi/domestic-stock/v1/trading/order-cash"
    URL = f"{URL_BASE}/{PATH}"
    body = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": code,
        "ORD_DVSN": "01", # 시장가
        "ORD_QTY": str(qty),
        "ORD_UNPR": "0",
    }
    headers = {
        "Content-Type": "applicatino/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC0801U", # 주식 현금 매도 주문
        "custtype": "P",
        "hashkey": hash_key(body)
    }
    # 매도 요청
    res = requests.post(URL, headers=headers, data=json.dumps(body))

    # 매도 요청 결과 저장
    success = res.json()['rt_cd']
    print(f"{res.json()['msg1']}")

    # 요청 결과 "0"이면 성공
    if success == '0':
        print(f"종목 코드 {code} {qty}주 매도에 성공하셨습니다.")
    # 아니면 실패
    else:
        print(f"종목 코드 {code} {qty}주 매도에 실패하셨습니다.")

# 액세스 토큰 발급
ACCESS_TOKEN = get_access_token()
print(f'접근 토근: {ACCESS_TOKEN}')

# 삼성전자우 종목 코드
stock_code = '005935'
# 1주
qty = 1

# 현재 시간 출력
print(f"현재 시간: {datetime.now()}")
# 삼성전자우 1주 매도 시도
sell_stock(stock_code, qty)
