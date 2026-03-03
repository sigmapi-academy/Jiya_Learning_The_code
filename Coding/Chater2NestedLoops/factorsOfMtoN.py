
M = int(input('Enter lower bound: '))
N = int(input('Enter upper bound: '))

if M >= N:
    print('Please enter lower bound and upper bound properly.')
else:
    while M <= N:
        f = 2
        if M > 1:
            print('Factor of', M,'= 1',end=', ')
        else:
            print('Factor of',M,'=', M)
            M += 1
            continue
        while f <= M/2:
            if M % f == 0:
                print(f, end=', ')
            f += 1
        print(M)
        M += 1
        