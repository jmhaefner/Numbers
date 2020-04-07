import sys

iterator = int(sys.argv[2])
k = int(sys.argv[1])
print('Collatzing', k)

def collatz(n):
    if n % iterator == 0:
        return n/iterator
    else:
        return 3*n+1
        return (iterator+(n % iterator))*n+(iterator-(n % iterator))

i = 0
imax = 100
while not k == 1 and not i >= imax:
    k = collatz(k)
    print(k)
    i += 1

print('DONE')

if not k == 1:
    print('FAILED TO CONVERGE')
