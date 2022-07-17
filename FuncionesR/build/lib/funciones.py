from rpy2.robjects import r

def returnPrimeNumbers(n):
    r.assign('n',n)
    r('''
    x = seq(1, n)
    prime_numbers=c()
    
    for (i in seq(2, n)) {
        if (any(x == i)) {
            prime_numbers = c(prime_numbers, i)
            x = c(x[(x %% i) != 0], i)
        }
    }
    print(prime_numbers)
    ''')