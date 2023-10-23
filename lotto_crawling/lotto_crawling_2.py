# 최근 로또 번호 전체를 출력

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 크롬 드라이버 설치 후 실행
driver = webdriver.Chrome(ChromeDriverManager().install())
# 최근 로또 번호 웹 페이지 접속
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2'
driver.get(url)

# 로또 웹 페이지에서 최근 1~6번 로또 번호 요소를 찾아서 번호를 가져옴
for i in range(1, 7):
    lotto_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(' + str(i) + ')').text
    print(f"당점번호{i}: {lotto_num}")

# 로또 웹 페이지에서 최근 보너스 번호 요소를 찾아서 번호를 가져옴
bonus_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
print(f"보너스번호: {bonus_num}")

# 크롬 드라이버 종료
driver.quit()