from datetime import datetime

now = datetime.now()
birthday = datetime(1999, 12, 6)
discharge_day = datetime(2021, 5, 21)
project_start_day = datetime(2023, 9, 19)

birthdays = now - birthday
discharge_days = now - discharge_day
project_start_days = now - project_start_day

print(f"본인 생성된지 +{birthdays.days}일째")
print(f"본인 전역한지 +{discharge_days.days}일째")
print(f"본인 미니 프로젝트 개시한지 +{project_start_days.days}일째")