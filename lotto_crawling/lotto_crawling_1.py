# 최근 로또 결과 중 1번째 번호를 웹 크롤링으로 출력

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 크롬 드라이버 설치 후 실행
driver = webdriver.Chrome(ChromeDriverManager().install())
# 최근 로또 번호 웹 페이지 접속
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2'
driver.get(url)
# 로또 웹 페이지에서 첫 번째 당첨번호 요소를 찾아서 번호를 가져옴
lotto_num1 = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(1)').text
# 첫 번째 당첨번호 출력
print(f"당점번호1 : {lotto_num1}")
# 크롬 드라이버 종료
driver.quit()