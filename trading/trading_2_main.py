# 실시간 주가 그래프 구현

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

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

# x축(시간) 저장할 20 길이 큐 생성
x = deque(maxlen=100)
# y1축(메모리 사용량) 저장할 20 길이 큐 생성
y = deque(maxlen=100)

plt.style.use('dark_background')

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

# 실시간으로 갱신되는 그래프 생성 함수
def animate(_):
    # 삼성전자우 현재 주가 획득
    current_price = get_current_price(stock_code)
    # 현재 시간을 큐 x에 추가
    x.append(datetime.now())
    # 현재 주가를 큐 y에 추가
    y.append(current_price)

    # 그래프 좌표축 제거
    plt.cla()
    # x(시간축)에 대한 y1(메모리 사용량)을 0.5 너비로 그래프에 표시
    plt.plot(x, y, label='current_price', linewidth=0.5)
    # 적당한 위치에 범례 표시
    plt.legend(loc='best')
    # 그래프에 격자를 0.3 투명도의 연파란색으로 추가
    plt.grid(True, color='lightblue', alpha=0.3)
    # y축 범위를 0~120으로 설정
    plt.ylim(53000, 55000)
    # y축 라벨 설정
    plt.ylabel('current_price')
    # x에 대한 y1 범위에 0.2 투명도로 색 추가
    plt.fill_between(x, y, alpha=0.2)
    # 그래프 제목 설정
    plt.title('Stock Price')

# 2초 간격으로 그래프 갱신
realtime_plot = FuncAnimation(plt.gcf(), animate, interval=2000)
# 그래프 출력
plt.show()

