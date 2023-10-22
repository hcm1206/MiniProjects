# 액셀 파일의 셀 값에 따라 글자 폰트 변경

import openpyxl
from openpyxl.styles import Font

# 액셀 파일의 데이터를 로드
wb = openpyxl.load_workbook('./test.xlsx', data_only=True)
# 액셀 파일에서 Sheet1 시트를 선택
ws = wb["Sheet1"]

# 액셀 파일 Sheet1 시트의 B열 전체 선택
cells = ws['B':'B']

# 폰트 크기가 20이고 진한 폰트(bold)가 활성화된 new_font 폰트 정보 저장
new_font = Font(size=20, bold=True)

# 폰트를 변경할 셀의 값 (white_list) 설정
white_list = ['김갑부', '정중산']

# Sheet1 시트의 B열 전체 셀 선택
for cell in cells:
    # 셀에 값이 존재하면
    try:
        # 셀의 값을 받아옴
        name = cell.value
        # 셀의 값이 white_list에 포함된 값이면
        if name in white_list:
            # 해당 셀의 폰트를 new_font 폰트 정보의 폰트로 설정
            cell.font = new_font
    # 셀에 값이 없으면 무시
    except:
        pass

# 설정한 내용의 액셀 정보를 xlsx 파일로 별도 저장
wb.save('test_result.xlsx')