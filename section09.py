# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환해야 함 !
f.close()

print("------------------------------")

# 예제 2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c)) # list로 형 변환도 가능
    print(iter(c)) # iterator로 반환해, for문에서도 활용 가능

print("------------------------------")

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        #print(c)
        print(c.strip())


print("------------------------------")

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content)

print("------------------------------")

# 예제 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end=' #### ')
        line = f.readline() # 한 문장 단위로 읽어올 때


# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ***** ')

print()

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line)) # 문자 -> int로 형변환
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))





# 파일 쓰기

# 예제 1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')


# 예제 2
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')


# 예제 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')


# 예제 4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)


# 예제 5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contests1!', file =f) # print문의 file 파라미터 활용 ! -> 콘솔로 나오지 않고 직접 파일에 찍힘
    print('Test Contests2!', file =f)


