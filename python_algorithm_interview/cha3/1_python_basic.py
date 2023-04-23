# 타입 힌트
a: str = "1"
# print(type(a))
b: int = 1

def fn(a: int) -> bool:
    pass

# map, filter 같은 함수형 기능 지원
c = list(map(lambda x: x+10, [1,2,3]))
# print(c)

# 리스트 컴프리헨션
d = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
# print(d)

# 만약 리스트 컴프리헨션을 사용하지 않는다면..
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)

# print(a)

# 딕셔너리도 가능
original = {'사과':1, '바나나':2}
a = {key : value for key, value in original.items()}
# print(a)

# 제너레이터 
# : 루프의 반복 동작을 제어할 수 있는 루틴 형태를 말함
# yield 구문을 사용하면 제너레이터를 리턴할 수 있다.
# 비교 : 기존 함수는 return 구문을 만나면 값을 리턴하고 모든 함수의 동작을 종료한다.
# yield는 중간값을 리턴한다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다. 

def get_naturl_number():
    n = 0 
    while True:
        n += 1
        yield n

# print(get_naturl_number())
# g = get_naturl_number()
# for _ in range(0, 10):
#     print(next(g))

# 제너레이터는 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능하다.
def generator():
    yield 1
    yield 'string'
    yield True

g = generator()
# print(next(g))
# print(next(g))
# print(next(g))

# range
a = [n for n in range(10000)]
b = range(10000)

# print(b)
# print(type(b))

import sys 
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# enumerate
# : 순서가 있는 자료형(list, set, tuple...)을 인덱스를 포함한 enumerate 객체로 리턴한다.
# : 인덱스 자동 부여 

a = [1,2,3,2,45,2]
# print(a)
# print(enumerate(a))
# print(list(enumerate(a)))

# for i, v in enumerate(a):
#     print(i, v)

# // 나눗셈 연산자
# print(5 / 3) # 값
# print(5 // 3) # 몫
# print(5 % 3) # 나머지 
# print(divmod(5, 3)) # 몫과 나머지

# print
print('A1', 'B2') # 한 칸 공백이 default
print('A1', 'B2', sep=',') # sep를 통해 구분자 지정
print('aa', end = ' ') # end를 통해 줄바꿈 지정 
print('bb')
a = ['A', 'B']
print(' '.join(a)) # 리스트를 출력할 때는 join으로 묶어서 처리

idx = 1
fruit = 'Apple'
print(f'{idx + 1}: {fruit}')

# pass
# : 널 연산으로 아무것도 하지 않는 기능이다.




