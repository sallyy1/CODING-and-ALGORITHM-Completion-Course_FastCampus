# Chapter06-03-1
# 파이썬 심화
# Futuer 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> Network I/O 관련 작업에 동시성 활용 권장
# 적합한 작업일 경우, 순차 진행보다 압도적으로 성능 향상

# 실습 대상 3가지 경우

# 순차 실행
# concurrent.futures 방법 1
# concurrent.futures 방법 2

# Google Python GIL(Global Interpreter Lock)
# Gil 은 한 번에 하나의 스레드만 수행할 수 있게 인터프리터 자체에서 락을 거는 것.

import os
import time
import sys
import csv
from concurrent import futures

# concurrent.futer 방법1(ThreadPoolExecutor, ProcessPoolExecutor)
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능
# 내부 과정 알 필요 없으며, 고수준으로 인터페이스 제공

# 국가 정보 선언
NATION_LS = ('Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()

# 초기 CSV 위치 지정
TARGET_CSV = '/Users/hyun/Desktop/FastCampus/python_test/resources/nations.csv'

# 저장 폴더 위치
DEST_DIR = '/Users/hyun/Desktop/FastCampus/python_test/csvs'

# CSV 헤더 기초 정보
HEADER = ['Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date','Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']

# 국가별 CSV 파일 저장
def save_csv(data, filename):
    # 최종 파일 저장할 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w', newline = '') as fp: # 줄바꿈 처리 안하기 위해
        writer = csv.DictWriter(fp, fieldnames= HEADER) # 열 머릿글
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)
    
 
# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        #print(reader.fieldnames) # 머릿글 확인 가능
        for r in reader:
            # OrderedDict 확인
            #print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data

# 중간 상황 출력
def show(text):
    print(text, end=' ') # 줄바꿈 처리 안하기 위해
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()

# 국가별 분리 함수 실행
def separate_many(nt):
    # 분리 데이터
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)

    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return len(nt_list)

# 시간 측정 및 메인함수
def main(separate_many):
    # worker 개수
    worker = min(20, len(NATION_LS)) # 9개

    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    with futures.ThreadPoolExecutor(worker) as excutor: # 9개의 쓰레드로 실행 됨
        end_tm = time.time() - start_tm(separate_many, sorted(NATION_LS))

    # 종료 시간
    end_tm = time.time()

    msg = '\n{} csv separated in {: 2f}s'
    # 최종 결과 출력
    print(msg.format(result_cnt, end_tm))



# 실행

if __name__ == '__main__':
    main(separate_many)



