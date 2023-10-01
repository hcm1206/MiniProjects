# 여러 개의 PDF 파일을 하나의 PDF 파일로 병합

from PyPDF2 import PdfFileReader, PdfFileMerger

# PDF 파일 병합 객체 생성
merger = PdfFileMerger()
# 첫 번째 PDF 파일을 불러와 읽기 객체 생성 후 병합 객체에 추가
merger.append(PdfFileReader(open("file1.pdf", 'rb')))
# 두 번째 PDF 파일을 불러와 읽기 객체 생성 후 병합 객체에 추가
merger.append(PdfFileReader(open("file2.pdf", 'rb')))
# 병합 객체의 모든 PDF 파일 페이지들을 별도 PDF 파일로 추출
merger.write("file1_2_merge.pdf")