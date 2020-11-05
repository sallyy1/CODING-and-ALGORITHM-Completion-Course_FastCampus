# Section11
# 파이썬 외부 파일 처리
# 파이썬, Excel, CSV 파일 읽기 및 쓰기


# CSV : MIME - text/csv

import csv

# 예제 1
with open('./resource/sample1.csv', 'r', encoding = 'euc-kr') as f:
    reader = csv.reader(f)
    # next(reader) -> Header(1행) 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # __iter__ 확인
    print()

    for c in reader:
        print(c)


# 예제 2
with open('./resource/sample2.csv', 'r', encoding = 'euc-kr') as f:
    reader = csv.reader(f, delimiter='|') # 구분자 옵션
    # next(reader) -> Header(1행) 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)


# 예제 3 (Dict변환)

with open('./resource/sample1.csv', 'r', encoding = 'euc-kr') as f:
    reader = csv.DictReader(f)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-------------------------')


# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', newline='', encoding = 'euc-kr') as f: # 줄바꿈 옵션 !
    wt = csv.writer(f)

    for v in w: # 순회하면서 작성
        wt.writerow(v) # row -> 하나하나 검증이 필요한 경우

# 예제 5
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', newline='', encoding = 'euc-kr') as f: # 줄바꿈 옵션 !
    wt = csv.writer(f)
    wt.writerows(w) # rows -> 이미 검증이 끝나, 한 번에 가져다 쓰면 되는 경우

    # dir 확인
    print(dir(wt))
    print(type(wt))


# XSL, XLSX (엑셀 처리)
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용 (openpyxl, xlrd를 판다스가 내부적으로 사용하기 때문)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# (옵션) : sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자
xlsx = pd.read_excel('./resource/sample.xlsx')


# 상위 데이터 확인
print(xlsx.head())

# 하위 데이터 확인
print(xlsx.tail())

# 행, 열 구조 데이터 확인
print(xlsx.shape)


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index = False, encoding = 'utf-8')
xlsx.to_csv('./resource/result.csv', index = False, encoding = 'utf-8')
