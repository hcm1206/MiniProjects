# 타이타닉 데이터셋 중 문자 데이터를 숫자로 변환

import seaborn as sns

# 타이타닉 데이터셋 데이터 프레임 로드
df = sns.load_dataset('titanic')
# 타이타닉 원본 데이터셋 출력
print(df, "\n")
# 타이타닉 원본 데이터셋의 데이터 요약 정보 출력
print(df.info())

# 타이타닉 원본 데이터셋의 컬럼(axis=1) 중 중복된 의미를 갖는 컬럼들을 제거한 데이터 프레임 생성
df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1)
# 불필요한 칼럼 제거 후의 데이터셋 출력
print(df1, "\n")
# 불필요한 칼럼 제거 후의 데이터셋 데이터 요약 정보 출력
print(df1.info())

# 수정된 데이터셋에서 age 속성이 누락(Null)된 행(axis=0)을 제거한 데이터 프레임 생성
df2 = df1.dropna(subset=['age'], how='any', axis=0)
# age 속성이 누락된 행 제거 후의 데이터셋 출력
print(df2, "\n")
# age 속성이 누락된 행 제거 후의 데이터셋 데이터 요약 정보 출력
print(df2.info())

# 수정된 데이터셋 중 embarked(탑승지 이름) 컬럼에서의 최빈값을 저장
freq_value = df2['embarked'].value_counts(dropna=True).idxmax()
# embarked(탑승지 이름) 최빈값 출력
print(freq_value)

# 수정된 데이터셋의 복사본 데이터 프레임 생성
df3 = df2.copy()
# 복사한 데이터셋에서 embarked 컬럼 중 결측값이 있을 경우 최빈값으로 대체
df3['embarked'].fillna(freq_value, inplace=True)
# 누락된 embarked 컬럼 대체 후의 데이터셋 출력
print(df3, "\n")
# 누락된 embarked 컬럼 대체 후의 데이터셋 데이터 요약 정보 출력
print(df3.info())

# 데이터셋에서 'sex' 컬럼을 확인하여 'male'이면 정수 1, 'female'이면 정수 0으로 대체
df3.loc[df3['sex'] == 'male', 'sex'] = 1
df3.loc[df3['sex'] == 'female', 'sex'] = 0

# 데이터셋에서 'embarked' 컬럼을 확인하여 각 속성 별 인덱스를 부여 후 속성을 인덱스 값으로 대체
for idx, item in enumerate(df3['embarked'].unique()):
    df3.loc[df3['embarked'] == item, 'embarked'] = idx

# 데이터셋에서 대체된 값들의 타입을 정수형으로 변환
df3 = df3.astype({'sex':'int', 'embarked':'int'})
# 범주형 문자 데이터 수치화 후의 데이터셋 출력
print(df3, "\n")
# 범주형 문자 데이터 수치화 후의 데이터셋 데이터 요약 정보 출력
print(df3.info())
