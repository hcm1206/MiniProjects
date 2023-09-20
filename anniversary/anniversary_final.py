from datetime import datetime, timedelta
import emoji

# 날짜 생성
now = datetime.now()
birthday = datetime(1999, 12, 6)
discharge_day = datetime(2021, 5, 21)
project_start_day = datetime(2023, 9, 19)

# 몇 일째인지 계산
birthdays = now - birthday
discharge_days = now - discharge_day
project_start_days = now - project_start_day

# 몇 일째인지 표시하는 문자열 생성
birthdays_result = emoji.emojize(f":birthday_cake: 본인 생성된지 +{birthdays}일째")
discharge_days_result = emoji.emojize(f":hiking_boot: 본인 전역한지 +{discharge_days}일째")
project_start_days_result = emoji.emojize(f":memo: 미니 프로젝트 개시한지 +{project_start_days}일째")

# 목표 일수(n일)를 설정
birthday_plus_days = 10000
discharge_day_plus_days = 1000
project_start_day_plus_days = 100

# 목표 일수(n일)에 다다르는 날짜 계산 
birthday_10000days = birthday + timedelta(days=birthday_plus_days)
discharge_day_1000days = discharge_day + timedelta(days=discharge_day_plus_days)
project_start_day_100days = project_start_day + timedelta(days=project_start_day_plus_days)

# 목표 일수에 다다르는 날짜를 표시하는 문자열 생성
birthday_plus_result = emoji.emojize(f":birthday_cake: 본인 생성된지 +{birthday_plus_days}일은 {birthday_10000days.year}년 {birthday_10000days.month}월 {birthday_10000days.day}일")
discharge_day_plus_result = emoji.emojize(f":hiking_boot: 본인 전역한지 +{discharge_day_plus_days}일은 {discharge_day_1000days.year}년 {discharge_day_1000days.month}월 {discharge_day_1000days.day}일")
project_start_day_plus_result = emoji.emojize(f":memo: 미니 프로젝트 개시한지 +{project_start_day_plus_days}일은 {project_start_day_100days.year}년 {project_start_day_100days.month}월 {project_start_day_100days.day}일")

# 최종 결과 출력
print(birthdays_result)
print(discharge_days_result)
print(project_start_days_result)
print()
print(birthday_plus_result)
print(discharge_day_plus_result)
print(project_start_day_plus_result)