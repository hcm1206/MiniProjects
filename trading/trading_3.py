# 계좌 보유 현금 조회

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

# 현재 계좌 잔고 반환하는 함수
def get_crash_balance() -> int:
    PATH = "uapi/domestic-stock/v1/trading/inquire-psbl-order"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC8908R", # 실전투자
        "custtype": "P", # 개인
    }
    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": "005935",
        "ORD_UNPR": "50000",
        "ORD_DVSN": "01",
        "CMA_EVLU_AMT_ICLD_YN": "Y",
        "OVRS_ICLD_YN": "Y"
    }
    res = requests.get(URL, headers=headers, params=params)
    cash_balance = int(res.json()['output']['ord_psbl_cash'])
    return cash_balance

# 액세스 토큰 발급
ACCESS_TOKEN = get_access_token()
print(f"접근 토큰: {ACCESS_TOKEN}")

# 계좌 잔고 획득
cash_balance = get_crash_balance()

# 현재 시간고 계좌 잔고 출력
print(f"현재 시간: {datetime.now()}")
print(f"현재 현금 잔고: {cash_balance}원")