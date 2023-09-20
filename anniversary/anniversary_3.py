from datetime import datetime, timedelta

plus_days = 10000
birthday = datetime(1999, 12, 6)
the_day = birthday + timedelta(days=plus_days)
print(f"본인 생성된지 +{plus_days}일은 {the_day.year}년 {the_day.month}월 {the_day.day}일")