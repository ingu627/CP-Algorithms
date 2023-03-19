if __name__ == '__main__':
    # from calcpkg.operation import mul, add, A
    #
    # print(add(10, 20))
    # print(A)
    # [print(i) for i in zip('1234', 'abcd')]
    # a = [1,2,3,4,5,6,7,8,9,10]
    # print(list(map(lambda x:str(x) if x % 3 == 0 else x, a)))

    # def func(x):
    #     return x > 5 and x < 10
    #
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    # print(list(filter(func, a)))

    from functools import reduce

    def f(x, y):
        return x + y

    a = [1,2,3,4,5]
    print(reduce(f, a))

