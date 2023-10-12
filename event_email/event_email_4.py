# 액셀 파일에서 조건에 맞는 데이터 행 추출
import pandas as pd

# 액셀에서 데이터 로드
df = pd.read_excel("./신검리스트.xlsx")
# 액셀 데이터 전체 원본 출력
print(df, "\n")

# 데이터 행 중 현역판정여부 속성이 'O'인 것만 추출
df_active_duty = df[df["현역판정여부"]=='O']
# 추출된 데이터 행 출력
print(df_active_duty, "\n")

# 현역판정여부 속성이 'O'인 데이터 행마다 반복
for idx, row in df_active_duty.iterrows():
    # 해당 데이터 행의 이름과 이메일 주소 표시
    print(f"{row['이름']}님의 이메일 {row['이메일주소']}으로 입영통지서 전송")