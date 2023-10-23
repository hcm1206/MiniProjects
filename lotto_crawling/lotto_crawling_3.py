# 역대 당첨번호에 가장 많이 등장한 번호 순으로 로또 번호 정렬

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from collections import Counter
import time
import re

# 크롬 드라이버 설치 후 실행
driver = webdriver.Chrome(ChromeDriverManager().install())
# 최근 로또 번호 웹 페이지 접속
url = "https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2"
driver.get(url)

# 로또 당첨 번호 숫자 담을 빈 리스트 생성
num_list = []
# 현재 로또 회차 번호 가져옴
now = re.sub(r'[^0-9]', '',driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > h4 > strong').text)

# 1회부터 현재 로또 회차 번호까지 반복
for i in range(1, int(now)):
    # 회차 조회 선택 부분에서 현재 i 회차에 해당한느 부분 선택
    select = Select(driver.find_element(By.CSS_SELECTOR, "#dwrNoList"))
    select.select_by_visible_text(str(i))
    # 조회 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, "#searchBtn").send_keys(Keys.ENTER)
    # 0.1초마다 반복
    time.sleep(0.1)

    # i회차 로또 당첨 번호 1~6개와 보너스 번호를 추출하여 리스트에 저장
    for j in range(1, 7):
        lotto_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(' + str(j) + ')').text
        num_list.append(lotto_num)

        bonus_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
        num_list.append(bonus_num)

# 리스트 안에 반복된 요소들의 반복 번호를 계산하여 출력(각 번호의 역대 등장 횟수 계산)
frequent_num = Counter(num_list)
print(frequent_num)
# 반복 요소들을 {'번호' : '번호 등장 횟수'}딕셔너리 형태로 저장
frequent_num_dict = dict(frequent_num)
# 딕셔너리를 번호 등장 횟수 순으로 정렬
sorted_frequent_num = sorted(frequent_num_dict.items(), key=lambda x: x[1], reverse=True)
# 정렬된 딕셔너리 출력
print(sorted_frequent_num)

# 크롬 드라이버 종료
driver.quit()