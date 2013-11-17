
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



