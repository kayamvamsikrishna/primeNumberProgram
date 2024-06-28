def isPrime(a):
    if a>1:
        for i in range(2,a//2):
            if a%i==0:
                return False
        else:
            return True
    else:
        False
if __name__=='__main__':
    ll=int(input('enter lower limit value='))
    ul=int(input('enter upper limit value='))
    for a in range(ll,ul+1):
        if isPrime(a):
            print(a,' ',end='')
