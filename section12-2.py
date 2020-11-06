# Section12-2.py
# 파이썬 데이터베이스 연동(SQLite)

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('/Users/hyun/Desktop/FastCampus/python_basic/resource/database.db') # 본인 DB 경로


# 커서 바인딩
c = conn.cursor()


# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
#print('One -> \n', c.fetchone())

# 지정 로우 선택
#print("Three -> \n", c.fetchmany(size = 3))

# 전체 로우 선택
#print("All -> \n", c.fetchall())
#print("All -> \n", c.fetchall()) # 여기서 한번 더 all을 하면, 커서가 DB 밖에 있기 때문에 [] 이 나옴.


# 순회 1
#rows = c.fetchall()
#for row in rows:
#    print('retrieve1 > ', row)

# 순회 2 (많이 사용)
#for row in c.fetchall():
#    print('retrieve2 > ', row)

# 순회3
for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    print('retrieve3 > ', row)


# WHERE Retrieve1
param1 = (3,) # 1) tuple로 바인딩 (물음표 ?)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 3번 이후 데이터에 대해서는 해당 데이터 없음


# WHERE Retrieve2
param2 = 4 # 2) integer로 바인딩 (퍼센트 %)
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall()) # 4번 이후 데이터에 대해서는 해당 데이터 없음


c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5}) # 3) dictionary로 바인딩 (정석)
print('param3', c.fetchone())
print('param3', c.fetchall()) # 5번 이후 데이터에 대해서는 해당 데이터 없음


# WHERE Retrieve4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?, ?)", param4)
print('param4', c.fetchall())


# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3, 4))
print('param5', c.fetchall())


# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())


# Dump 출력 (중요 !) -> 데이터베이스 백업
with conn: # with문을 사용하면, 자동으로 close()로 해제해줌
    with open('/Users/hyun/Desktop/FastCampus/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line) # iterator -> 한 줄 한 줄 쓰기
        print('Dump Print Complete')

# f.close() 함수도 호출됐고, conn.close() 함수도 호출이 됨.
