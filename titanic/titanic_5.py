# 타이타닉 데이터셋의 데이터 정규화(스케일링)

import seaborn as sns

# 타이타닉 데이터셋 데이터 프레임 로드
df = sns.load_dataset('titanic')
# 원본 데이터셋에서 중복된 의미를 지닌 컬럼 제거
df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1)
# 수정된 데이터셋에서 나이 정보가 누락된 행 제거
df2 = df1.dropna(subset=['age'], how='any', axis=0)
# 수정된 데이터셋에서 탑승지의 최빈값 계산
freq_value = df2['embarked'].value_counts(dropna=True).idxmax()
# 수정된 데이터셋 복사본 생성
df3 = df2.copy()
# 복사본 데이터셋에서 탑승지가 누락된 행의 탑승지를 최빈값으로 대체
df3['embarked'].fillna(freq_value, inplace=True)
# 수정된 데이터셋의 성별 속성에서 남자를 1, 여자를 0으로 수치화
df3.loc[df3['sex'] == 'male', 'sex'] = 1
df3.loc[df3['sex'] == 'female', 'sex'] = 0

# 수정된 데이터셋의 탑승지 속성을 인덱스화하여 수치화
for idx, item in enumerate(df3['embarked'].unique()):
    df3.loc[df3['embarked'] == item, 'embarked'] = idx

# 수정된 데이터셋에서 수치화된 속성 타입을 정수형으로 변경
df3 = df3.astype({'sex':'int', 'embarked':'int'})

# 수정된 데이터셋 수치를 0~1 사이 범위로 정규화(스케일링)
df3 = (df3 - df3.min()) / (df3.max() - df3.min())
# 수정된 데이터셋 최종본 출력
print(df3)

# 수정된 데이터셋에서 생존 여부별로 구분하여 각 수치의 평균값 출력
print(df3.groupby(['survived']).mean())