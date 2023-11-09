# 로그 메시지 포맷 변경

import coloredlogs, logging

# 로거 객체 생성하여 현재 코드의 로거로 활용
logger = logging.getLogger(__name__)
# 컬러 로그를 설치(디버깅용 레벨 이상을 출력, 포멧은 {레벨명} - {메시지 내용}({발생 시간}) 형식)
coloredlogs.install(level='DEBUG', fmt='%(levelname)s - %(message)s(%(asctime)s)')

# debug 레벨의 로그 메시지 출력
logging.debug("디버깅 메시지입니다.")
# info 레벨의 로그 메시지 출력
logging.info("정보성 메시지입니다.")
# warning 레벨의 로그 메시지 출력
logging.warning("경고 메시입니다.")
# error 레벨의 로그 메시지 출력
logging.error("에러 메시지입니다.")
# critical 레벨의 로그 메시지 출력
logging.error("치명적 에러 메시지입니다.")