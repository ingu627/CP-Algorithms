# 리스트 활용 방법

# 선언
a = list()
a = []

a = [1, 2, 3]
print(a)

a.append(4)
print(a)

# insert() : 특정 위치의 인덱스를 지정해 요소 추가
a.insert(2, 5)
print(a)

# 리스트는 숫자 외에 다양한 자료형을 단일 리스트에 관리할 수 있다.
a.append('안녕')
a.append(True)
print(a)

# 해당 인덱스의 값 가져오기
print(a[2])

# 존재하지 않는 인덱스를 조회할 경우 다음과 같이 IndexError가 발생
# a[9]

# try 구문으로 에러에 대한 예외 처리
try:
    print(a[9])
except IndexError:
    print('존재하지 않는 인덱스')

# 리스트에서 요소를 삭제하는 2가지방법 : 인덱스로 삭제, 값으로 삭제
# del 키워드로 인덱스의 위치에 있는 요소 삭제
del a[1]
print(a)

# remove() 함수를 사용해 값에 해당하는 요소 삭제
a.remove(3)
print(a)

# pop() 함수를 사용하면 스택의 팝 연산처럼 추출로 처리됨
# 즉, 삭제될 값을 리턴하고 삭제가 진행된다.

a.pop(3)
print(a)
