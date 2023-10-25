# kNN 알고리즘을 활용하여 타이타닉 생존 여부 예측

import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# 타이타닉 데이터셋 데이터 프레임 로드
df = sns.load_dataset('titanic')
# 원본 데이터셋에서 중복된 의미를 지닌 컬럼 제거
df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1)
# 수정된 데이터셋에서 나이 정보가 누락된 행 제거
df2 = df1.dropna(subset=['age'], how='any', axis=0)
# 수정된 데이터셋에서 탑승지의 최빈값 계산
freq_value = df2['embarked'].value_counts(dropna=True).idxmax()
# 수정된 데이터셋의 복사본 생성
df3 = df2.copy()
# 복사본 데이터셋에서 탑승치가 누락된 행의 탑승지를 최빈값으로 대체
df3['embarked'].fillna(freq_value, inplace=True)
# 수정된 데이터셋의 성별 속성에서 남자를 1, 여자를 0으로 수치화
df3.loc[df3['sex'] == 'male', 'sex'] = 1
df3.loc[df3['sex'] == 'female', 'sex'] = 0

# 수정된 데이터셋의 탑승지 속성을 인덱스화하여 수치화
for idx, item in enumerate(df3['embarked'].unique()):
    df3.loc[df3['embarked'] == item, 'embarked'] = idx

# 수정된 데이터셋에서 수치화된 속성 타입을 정수형으로 변경
df3 = df3.astype({'sex':'int', 'embarked':'int'})

# 최종 수정 데이터셋에서 생존여부를 제외한 속성을 입력값 X 데이터로 분류
X = df3[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]
# 최종 수정 데이터셋에서 생존여부를 출력값 y 데이터로 분류
y = df3['survived']

# X 데이터를 정규화(스케일링)
X = preprocessing.StandardScaler().fit(X).transform(X)
# X, y 데이터를 7 : 3 비율로 훈련 데이터와 테스트 데이터로 랜덤 구분
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

# 근접 이웃(k)를 5로 설정하여 knn(최근접 이웃) 분류기 객체 생성
knn = KNeighborsClassifier(n_neighbors=5)
# knn 분류기에 X, y 훈련 데이터 입력하여 최적화
knn.fit(X_train, y_train)
# 최적화된 knn 분류기에 X 테스트 데이터 입력하여 출력값(생존여부) 예측
y_pred = knn.predict(X_test)
# knn 분류기의 y데이터 예측값과 실제값 비교하여 정확도 계산
acc = metrics.accuracy_score(y_test, y_pred)
# 정확도 출력
print("예측 정확도:", acc)
