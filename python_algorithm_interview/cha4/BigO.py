# 각 계산 결과를 보여주는 코드
# for n in range(1, 15 + 1):
#     print(n, n ** 2, 2 ** n)

print(True == 1)
print(False == 0)

a = {'a', 'b', 'c'}
print(type(a))
a = {'a':'A', 'b':'B', 'c':'C'}
print(type(a))

# 불변 객체
10
c = 10
d = c
print(id(10), id(c), id(d))

# 가변 객체
e = [1,2,3,4,5]
f = e
e[2] = 4

print(e)
print(f)