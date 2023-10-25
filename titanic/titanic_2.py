# 타이타닉 데이터셋 중 불필요한 컬럼 제거

import seaborn as sns

# 타이타닉 데이터셋의 데이터 프레임 로드
df = sns.load_dataset('titanic')
# 타이타닉 원본 데이터셋 출력
print(df, '\n')
# 타이타닉 원본 데이터셋의 데이터 요약 정보 출력
print(df.info())

# 타이타닉 원본 데이터셋의 컬럼(axis=1) 중 중복된 의미를 갖는 컬럼들을 제거한 데이터 프레임 생성
df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town'], axis=1)
# 불필요한 컬럼 제거 후의 데이터셋 출력
print(df1, '\n')
# 불필요한 컬럼 제거 후의 데이터셋 데이터 요약 정보 출력
print(df1.info())