#質數 除了1與自己之外都不能整除的數
def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
print(is_prime(11))
print(is_prime(8))
