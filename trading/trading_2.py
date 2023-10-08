# 2초마다 삼성전자우 주가 확인

import yaml
import requests
import json
from datetime import datetime
import time

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

# 입력받은 종목코드에 대한 주가를 반환하는 함수
def get_current_price(code: str) -> int:
    PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "FHKST01010100"
    }
    params = {
        "fid_cond_mrkt_div_code": "J", # 주식, ETF, ETN
        "fid_input_iscd": code,
    }
    res = requests.get(URL, headers=headers, params=params)
    current_price = int(res.json()['output']['stck_prpr'])
    return current_price

# 액세스 토큰 발급
ACCESS_TOKEN = get_access_token()
print(f"접근 토큰: {ACCESS_TOKEN}")

# 삼성전자우 종목 코드
stock_code = "005935"

while True:
    # 삼성전자우 현재 주가 획득
    current_price = get_current_price(stock_code)
    # 현재 시간과 삼성전자우 주가 출력
    print(f"현재 시간: {datetime.now()}")
    print(f"현재 주가: {current_price}원")

    # 2초마다 반복
    time.sleep(2)
