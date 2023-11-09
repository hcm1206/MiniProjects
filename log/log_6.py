# 로그 포맷에 적용 가능한 모든 속성을 적용하여 출력

import coloredlogs, logging

# 레벨 별 로그 메시지 출력하는 함수 정의
def show_log():
    # debug 레벨의 로그 메시지 출력
    logging.debug("디버깅 메시지입니다.")
    # info 레벨의 로그 메시지 출력
    logging.info("정보성 메시지입니다.")
    # warning 레벨의 로그 메시지 출력
    logging.warning("경고 메시지입니다.")
    # error 레벨의 로그 메시지 출력
    logging.error("에러 메시지입니다.")
    # critical 레벨의 로그 메시지 출력
    logging.critical("치명적 에러 메시지입니다.")

# 로거 객체 생성하여 현재 코드의 로거로 활용
logger = logging.getLogger(__name__)
# 컬러 로그를 설치(디버깅용 레벨 이상을 출력, 
# 포맷은 {발생 시간} {time.time() 형식의 발생 시간} {파일명} {함수명} {레벨명} {레벨번호} {코드 라인 위치} {메시지 내용} {프로세스 ID} 
# {logging 모듈 로드 이후 지난 밀리초} {스레드ID} {스레드명} 후 줄바꿈)
coloredlogs.install(level='DEBUG',
                    fmt='''%(asctime)s %(created)f %(filename)s %(funcName)s
                    %(levelname)s %(levelno)s %(lineno)d %(message)s %(processName)s
                    %(relativeCreated)d %(thread)d %(threadName)s \n
                    ''')

# 레벨 별 로그 메시지 출력
show_log()