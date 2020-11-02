class Fibonacci:
    def __init__(self, title="fibonacci"): # title 값이 넘어오면 그 값을 사용하고, 넘어오지 않으면 기본값으로 "fibonacci"를 사용하겠다는 옵션
        self.title = title

    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a,b = b, a+b
        print() # 줄바꿈


    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a,b = b, a+b
        return result