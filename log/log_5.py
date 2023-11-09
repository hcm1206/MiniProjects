# 로그 메시지 포맷에 로그가 발생한 파일명과 코드 라인 위치를 추가

import coloredlogs, logging

# 로거 객체 생성하여 현재 코드의 로거로 활용
logger = logging.getLogger(__name__)
# 컬러 로그를 설치(디버깅용 레벨 이상을 출력, 포맷은 [{발생 시간}] {파일명}:{코드 라인 위치} [{레벨명}] {메시지 내용})
coloredlogs.install(level='DEBUG', fmt='[%(asctime)s] %(filename)s:%(lineno)d [%(levelname)s] %(message)s')

# debug 레벨의 로그 메시지 출력
logging.debug("디버깅 메시지입니다.")
# info 레벨의 로그 메시지 출력
logging.info("정보성 메시지입니다.")
# warning 레벨의 로그 메시지 출력
logging.warning("경고성 메시지입니다.")
# error 레벨의 로그 메시지 출력
logging.error("에러 메시지입니다.")
# critical 레벨의 로그 메시지 출력
logging.critical("치명적 에러 메시지입니다.")