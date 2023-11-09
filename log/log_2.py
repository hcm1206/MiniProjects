# 콘솔에 일반 에러 로그 대신 라이브러리를 활용한 컬러 로그 출력

import coloredlogs, logging

# 로거 객체 생성하여 현재 코드의 로거로 사용
logger = logging.getLogger(__name__)
# 컬러 로그를 설치(디버깅용 레벨 이상을 출력)
coloredlogs.install(level='DEBUG')

# 인덱스가 4까지 존재하는 리스트 생성
a = [1, 2, 3, 4, 5]

# 리스트의 인덱스 6번 원소 출력 시도
try:
    print(a[6])
# 예외 발생 시 해당 예외에 대한 로깅 에러 메시지 출력
except Exception as e:
    logging.error(e)

# 로깅 메시지로 프로그램 종료 출력
logging.info('프로그램 종료!')