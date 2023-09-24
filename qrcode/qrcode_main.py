import qrcode

while True:
    print("QR코드 생성기입니다.")
    
    while True:
        try:
            url = input("QR코드를 생성할 URL 링크를 입력하세요 : ")
        except:
            print("경고 : 입력 중 예상치 못한 오류가 발생했습니다.\n")
            continue
        break

    qrcode_img = qrcode.make(url)

    while True:
        try:
            file_name = input("QR코드 이미지 파일명을 입력하세요 : ")
        except:
            print("경고 : 입력 중 예상치 못한 오류가 발생했습니다.\n")
            continue
        break
    
    try:
        qrcode_img.save('./' + str(file_name) + '.png')
    except:
        print("경고 : 이미지 저장 중 예상치 못한 오류가 발생했습니다.\n")
        continue

    print(str(url) + " URL 링크에 대한 QR코드 이미지 파일이 " + str(file_name) + '.png 파일로 저장되었습니다.\n')
    



