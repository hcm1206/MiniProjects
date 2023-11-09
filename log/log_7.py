# 로그를 텍스트 파일로 저장

import logging

# 로거 객체 생성하여 현재 코드의 로거로 활용
logger = logging.getLogger(__name__)
# 로거가 디버깅용 레벨 이상을 출력하도록 설정
logger.setLevel(logging.DEBUG)

# [{발생 시간}] {파일명}:{코드 라인 위치} [{레벨명}] {메시지 내용} 형식의 로그 포맷 저장
formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d [%(levelname)s] %(message)s')
# utf-8로 인코딩된 log.txt 텍스트 파일 핸들러 저장
file_handler = logging.FileHandler('./log.txt', encoding='utf-8')
# 파일 핸들러에 지정한 로그 포맷을 설정
file_handler.setFormatter(formatter)
# 로거에 파일 핸들러 적용(로그가 파일 핸들러에 지정된 형식으로 텍스트 파일로 저장됨)
logger.addHandler(file_handler)

# debug 레벨의 로그 메시지 생성(텍스트 파일에 저장)
logger.debug("디버깅 메시지입니다.")
# info 레벨의 로그 메시지 생성(텍스트 파일에 저장)
logger.info("정보성 메시지입니다.")
# warning 레벨의 로그 메시지 생성(텍스트 파일에 저장)
logger.warning("경고 메시지입니다.")
# error 레벨의 로그 메시지 생성(텍스트 파일에 저장)
logger.error("에러 메시지입니다.")
# critical 레벨의 로그 메시지 생성(텍스트 파일에 저장)
logger.critical("치명적 에러 메시지입니다.")