def prime_factors(n):
    """按照非递减顺序打印因子

    >>> prime_factors(8)
    2
    2
    2
    """
    while n > 1 :
        k = smallest_prime_factor(n)
        n //= k
        print(k)

def smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k = k + 1
    return  k



def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
chocolate = cake()

