# 클래스를 사용하지 않은 사람 소개 코드


# 입력받은 이름, 직업, 성별을 이용해 소개글 출력하는 함수 정의
def introduce(name, job, sex):
    print(f"{name}의 직업은 {job}이고 성별은 {sex}입니다.")

# 1번째 사람의 이름, 직업, 성별 값 저장
name1 = '김철수'
job1 = '개발자'
sex1 = '남자'
# 1번째 사람의 소개글 출력
introduce(name1, job1, sex1)

# 2번째 사람의 이름, 직업, 성별 값 저장
name2 = '아이유'
job2 = '가수'
sex2 = '여자'
# 2번째 사람의 소개글 출력
introduce(name2, job2, sex2)

# 3번째 사람의 이름, 직업, 성별 값 저장
name3 = '손흥민'
job3 = '축구선수'
sex3 = '남자'
# 3번째 사람의 소개글 출력
introduce(name3, job3, sex3)