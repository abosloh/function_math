# if number x is odd return true else false
def is_odd(x):
    if x%2!=0: return True
    else: return False
  


# if number num is composite return true else false
# composite number can divied by number other than 1 and itslef (not prime)
def is_composite(num):
    if num < 4 : return False
    for n in range(2,int(num**0.5+1)):
        if num%n == 0:
            return True
    return False


# return list of divisors of the number
# print get_factors(28)
# the output will be 
# [1, 2, 4, 7, 14, 28]
def get_factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)   ) ))
