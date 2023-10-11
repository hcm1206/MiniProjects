# 주식 트레이드 관련 함수 코드

import yaml
import requests
import json

# API 키와 계좌 정보 등 로드
with open('config.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

# 설정값 변수로 저장
APP_KEY = cfg['APP_KEY']
APP_SECRET = cfg['APP_SECRET']
CANO = cfg['CANO']
ACNT_PRDT_CD = cfg['ACNT_PRDT_CD']
URL_BASE = cfg['URL_BASE']

# 액세스 토큰 발급 함수
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

# 해시 키 발급 함수
def hash_key(body):
    PATH = "uapi/hashkey"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        'content-Type': 'application/json',
        'appkey': APP_KEY,
        'appSecret': APP_SECRET,
    }    
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    hashkey = res.json()["HASH"]
    return hashkey

# 입력받은 종목 코드의 주가 확인 함수
def get_current_price(code):
    PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "FHKST01010100" # 주식 현재가 시세
    }
    params = {
        "fid_cond_mrkt_div_code": "J", # 주식, ETF, ETN
        "fid_input_iscd": code,
    }
    res = requests.get(URL, headers=headers, params=params)
    current_price = int(res.json()['output']['stck_prpr'])
    return current_price

# 현재 계좌 잔고 출력 함수
def get_cash_balance():
    PATH = "uapi/domestic-stock/v1/trading/inquire-psbl-order"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC8908R",
        "custtpye": "P",
    }
    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": "005935", # 현금 잔고 조회 목적이므로 아무 종목번호를 입력해도 됨
        "ORD_UNPR": "50000", # 한금 잔고 조회 목적으므로 1주당 가격을 아무렇게나 입력해도 됨
        "ORD_DVSN": "01", # 시장가
        "CMA_EVLU_AMT_ICLD_YN": "Y", # CMA평가금액포함
        "OVRS_ICLD_YN": "Y" # 해외포함
    }
    res = requests.get(URL, headers=headers, params=params)
    cash_balance = int(res.json()['output']['ord_psbl_cash'])
    return cash_balance

# 현재 보유 주식 잔고 출력 함수
def get_stock_balance():
    PATH = "uapi/domestic-stock/v1/trading/inquire-balance"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC8434R",
        "custtype": "P"
    }
    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "",
        "INQR_DVSN": "02", # 조회구분 - 종목별
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N", # 펀드결제분포함여부 - 포함하지 않음
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "00",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }
    res = requests.get(URL, headers=headers, params=params)
    stock_list = res.json()['output1']

    for i, stock in enumerate(stock_list):
        print(f"{i+1}. {stock['prdt_name']}({stock['pdno']})")
        print(f"\t보유수량: {stock['hldg_qty']}주")
        print(f"\t평가금액: {stock['evlu_amt']}원")
        print(f"\t매입금액: {stock['pchs_amt']}원")
        print(f"\t평가손익금액: {stock['evlu_pfls_amt']}원\n")

# 입력받은 종목 코드에 해당하는 주식을 입력된 주만큼 매수하는 함수
def buy_stock(code, qty):
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
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC0802U",
        "custtype": "P", # 개인
        "hashkey": hash_key(body)
    }
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    print(res.json())
    success = res.json()['rt_cd']
    print(f"{res.json()['msg1']}")

    if success == '0':
        print(f"종목 코드 {code} {qty}주 매수에 성공하셨습니다.")
    else:
        print(f"종목 코드 {code} {qty}주 매수에 실패하셨습니다.")

# 입력받은 종목 코드에 해당하는 주식을 입력된 주만큼 매도하는 함수
def sell_stock(code, qty):
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
        "Content-Type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC0801U",
        "custttype": "P",
        "hashkey": hash_key(body)
    }
    res = requests.post(URL, headers=headers, data=json.dumps(body))

    success = res.json()['rt_cd']
    print(f"{res.json()['msg1']}")

    if success == "0":
        print(f"종목 코드 {code} {qty}주 매도에 성공하셨습니다.")
    else:
        print(f"종목 코드 {code} {qty}주 매도에 실패하셨습니다.")

# 액세스 토큰 발급하여 값으로 저장
ACCESS_TOKEN = get_access_token()
