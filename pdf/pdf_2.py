# 여러 장의 PDF 페이지 추출

from PyPDF2 import PdfFileReader, PdfFileWriter

# PDF 파일 로드
with open("pdf_test1.pdf", 'rb') as PDFfile:
    # 불러온 PDF 파일을 읽기 객체로 저장
    reader = PdfFileReader(PDFfile)
    # PDF 파일 쓰기 객체 생성
    writer = PdfFileWriter()
    # 쓰기 객체에 읽기 객체 0번 인덱스(1번째) 페이지 추가
    writer.addPage(reader.getPage(0))
    # 쓰기 객체에 읽기 객체 2번 인덱스(3번째) 페이지 추가
    writer.addPage(reader.getPage(2))
    # 쓰기 객체에 읽기 객체 4번 인덱스(5번째) 페이지 추가
    writer.addPage(reader.getPage(4))
    # 쓰기 객체에 저장된 PDF 페이지들을 별도 PDF 파일로 추출
    writer.write(open("page1_3_5.pdf", 'wb'))