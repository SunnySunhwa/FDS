def gen(iterable):
    for e in iterable:
        yield e

def fibo(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

def counter(low, high):
    cnt = low

    while cnt <= high:
        yield cnt
        cnt += 1

if __name__ == "__main__":
    li = [1, 2, 3, 4]
    #제너레이터 생성
    g = gen(li)
    
    print(type(g))
    
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    #print(next(g))

    for num in fibo(10):
        print(num, end = '  ')

    print('')

    c = counter(4, 10)
    for cnt in c:
        print(cnt, end = '  ')
        
