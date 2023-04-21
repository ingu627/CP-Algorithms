if __name__ == "__main__":
    a, b, c = map(int, input().split())
    amount = 0
    if a == b and b == c and c == a:
        amount = 10000 + 1000*a
        print(amount)
    elif a == b or b == c:
        amount = 1000 + b*100
        print(amount)
    elif a == c:
        amount = 1000 + a*100
        print(amount)
    else:
        amount = max(a, b, c) *100
        print(amount)

