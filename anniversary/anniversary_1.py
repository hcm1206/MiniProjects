from datetime import datetime

now = datetime.now()
birthday = datetime(1999, 12, 6)
birthdays = now - birthday
print(f"본인 생성된지 +{birthdays.days}째")