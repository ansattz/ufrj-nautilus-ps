import readline
# 1
def verifyFLItens(l):
    ''' using the index i can check if the first(index:0) and 
    the last one(index:-1) are equal'''
    if l[0] == l[-1]:
        return True
    else:
        return False

# 2
def primeCheck(n):
    ''' add all divs of n in the list and check if the list of divs 
    is different of 2 two '''
    allDivsOfn=[]
    for i in range(1,n+1):
        if n%i == 0:
            allDivsOfn.append(i)
        i+=1
    if len(allDivsOfn) != 2:
        return False
    else:
        return True

def primeDivisor(m):
    ''' add all divs of m in the list, check if each element of 
    the first list is a prime and return a list of prime divisors '''
    allDivsOfm = []
    primeDivs=[]
    for i in range(1, m+1):
        if m%i == 0:
            allDivsOfm.append(i)
        i+=1
    for j in allDivsOfm:
        if primeCheck(j) == True:
            primeDivs.append(j)
    return primeDivs

def maxPrimeDiv(m):
    ''' return value of the max element in the list of prime divisors '''
    return max(primeDivisor(m))

# 3
def palin(x):
    ''' doesnt matter if it is a string or an integer, 
    so i can use the reverse trick that are common used in lists '''
    xRev = x[::-1]
    if x == xRev:
        return xRev
    else:
        return False

# 4
def primeSum():
    ''' check if each integer from 1 to 999 is a prime and
    sum every of these primes'''
    l = []
    for i in range(1,1000):
        if primeCheck(i):
            l.append(i)
    return sum(l)

def menu():
    print('========= MENU =========')
    print('')
    print('1 - Checks if the first item is the same as the last one of a list')
    print('2 - Greatest prime divisor of a number')
    print('3 - Checks if the number is a palindrome')
    print('4 - Sum of all primes less than 1000')
    print('0 - Close Entregavel 1')
    print('')
    print('==================================')

while True:
    menu()

    option = input('Choose an option: ')
    if option == '1':
        print('')
        print('1 - You are give me a list')
        print('2 - You are give me itens for the list')
        print('')
        solvingAmbig = input('Give me more info(choose an option): ')
        print('')
        if solvingAmbig == '1':
            stringList = input('Give me the list(without space between commas): ')
            print('')
            realList = stringList.strip('][').split(',')
            if verifyFLItens(realList) == True:
                print('The first item is the same as the last')
                print('')
                continue
            elif verifyFLItens(realList) == False:
                print('The first item IS NOT the same as the last')
                print('')
                continue
            else:
                print('Invalid list')
                print('')
                continue
        elif solvingAmbig == '2':
            numbers = list(map(int,input("""Give me the itens(with space
                between them: """).strip().split()))
            print('')
            if verifyFLItens(numbers) == True:
                print('The first item is the same as the last')
                print('')
                continue
            elif verifyFLItens(numbers) == False:
                print('The first item IS NOT the same as last')
                print('')
                continue
            else:
                print('Invalid input to create a list')
                print('')
                continue
        else:
            print('')
            print('======> Invalid option')
            print('')
            continue
    elif option == '2':
        m = int(input("Give me a number: "))
        print('')
        print(str.format('The greatest prime divisor of {} is: {}', m,
            maxPrimeDiv(m)))
        print('')
    elif option == '3':
        x = input("Give me a number: ")
        if palin(x) != False:
            print('')
            print(str.format('The number {} is a palindrome',x))
            print('')
        else:
            print('')
            print(str.format('The number {} IS NOT a palindrome',x))
            print('')
    elif option == '4':
        print('')
        print(str.format('The sum of all primes less than 1000 is: {}',
            primeSum()))
        print('')
    elif option == '0':
        print('')
        print("""\u001b[34m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⢀⣤⣤⡄⠀⠀⠀⠀⠀⣴⣶⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡄⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠋⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢤⣤⠄⠀⠀⢤⡤⠄⢤⡤⠤⢤⡄⠠⢤⡤⠤⣄⠀⠀⢤⣤⠄⢀⣀⣀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠀⠀⠀⠀⡇⠀⢸⡇⠀⢀⠁⠀⢸⡇⠀⣹⡇⠀⠀⣿⠀⢸⣿⣿⣦⠀⢸⣿⠀⣀⣀⣀⡀⠀⣀⡀⠀⣀⣀⣀⣾⣇⡀⣈⣉⡀⣿⡇⢀⣀⠀⢀⣀⠀⠀⣀⣀⣀⠀⠀
⠀⠀⠀⣿⠀⠀⠀⠀⡇⠀⢸⡟⠒⠻⠀⠀⢸⡗⢶⣏⠀⠀⠀⣿⠀⢸⣿⡇⢻⣧⣸⣿⠀⣻⣭⣿⣷⠀⣿⡇⠀⣿⣿⠉⣿⡏⠁⣿⣿⡇⣿⡇⢸⣿⠀⢸⣿⠀⣿⣿⣭⣉⠀⠀
⠀⠀⠀⢿⣄⠀⠀⣸⠃⠀⢸⡇⠀⠀⠀⠀⢸⡇⠀⢿⣄⠀⠀⣿⠀⢸⣿⡇⠀⢻⣿⣿⢸⣿⣃⣼⣿⠀⢿⣧⣀⣿⣿⠀⣿⣇⡀⣿⣿⡇⣿⡇⢸⣿⣄⣸⣿⠀⣀⣘⣻⣿⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠋⠙⠃⠀⠀⠙⠋⠙⠀⠀⠉⠃⣸⠏⠀⠈⠉⠁⠀⠀⠉⠉⠀⠉⠉⠉⠉⠀⠈⠉⠉⠉⠉⠀⠈⠉⠁⠉⠉⠁⠉⠁⠀⠉⠉⠉⠉⠀⠉⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        \u001b[0m""")
        print('')
        break
    else:
        print('')
        print('======> Invalid option')
        print('')
