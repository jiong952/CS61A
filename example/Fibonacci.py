def fib(n):
    """计算斐波那契数列 N >= 1"""
    pre, cur = 0, 1
    k = 1
    while k < n:
        pre, cur = cur, pre + cur
        k += 1
    return cur
print(fib(6))

def make_adder(n):
    def adder(k):
        return k + n
    return adder

print(make_adder(2)(1))