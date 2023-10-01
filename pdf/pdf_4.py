# PDF 파일에서 텍스트 추출

from PyPDF2 import PdfFileReader

# PDF 파일 로드
with open("pdf_test2.pdf", 'rb') as PDFfile:
    # 불러온 PDF 파일을 읽기 객체로 저장
    reader = PdfFileReader(PDFfile)

    # 불러온 PDF 파일에서 각 페이지 별로 반복
    for i in range(reader.numPages):
        # 현재 페이지 번호 출력
        print(f"{i+1}페이지>>\n")

        # 현재 페이지 번호에 해당하는 PDF 페이지 로드
        pages = reader.getPage(i)
        # 현재 페이지의 텍스트 추출
        extracted_text = pages.extractText()
        # 추출된 텍스트 출력
        print(extracted_text)