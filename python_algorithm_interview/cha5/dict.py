# 딕셔너리

# 선언
a = dict()
a = {}

a = {'key1' : 'value1', 'key2' : 'value2'}
print(a)
a['key3'] = 'value2'
print(a)

# 딕셔너리의 키를 지정하면 값을 조회할 수 있다.
print(a['key1'])


# 존재하지 않는 키가 있을 경우 예외 처리를 하게 되면, 나중에 추가 작업을 할 수 있어 유용.
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

# 딕셔너리의 items() 메소드를 사용하면 키와 값을 각각 꺼내올 수 있다.
for k, v in a.items():
    print(k, v)

# defaultdict 객체
from collections import defaultdict

b = defaultdict(int)
b['A'] = 5
b['B'] = 4
print(b)
b['C'] += 2
print(b)

# Counter

from collections import Counter

c = [1,2,3,4,5,5,5,6,6]
d = Counter(c)
print(d)

# most_common()

print(d.most_common(2))
