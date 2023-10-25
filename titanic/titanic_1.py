# 타이타닉 데이터셋 확인

import seaborn as sns

# 타이타닉 데이터셋의 데이터 프레임 로드
df = sns.load_dataset('titanic')
# 타이타닉 데이터셋 출력
print(df, "\n")
# 타이타닉 데이터셋의 데이터 요약 정보 출력
print(df.info())