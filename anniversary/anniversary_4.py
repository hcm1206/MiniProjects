from datetime import datetime, timedelta
import emoji

plus_days = 10000
birthday = datetime(1999, 12, 6)
the_day = birthday + timedelta(days=plus_days)
result = emoji.emojize(f":birthday_cake: 본인 생성된지 +{plus_days}일은 {the_day.year}년 {the_day.month}월 {the_day.day}일")
print(result)