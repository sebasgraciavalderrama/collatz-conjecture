def caculate_collatz(n, steps):
    print(f'Number: {n}')
    steps+=1
    if n == 1:
        print(f'Cycle ended with 1 \nNumber of steps: {steps}')
        return
    if n % 2 == 0:
        caculate_collatz(n/2, steps)
    else:
        caculate_collatz(((3*n)+1)/2, steps)

if __name__ == '__main__':
    n = 0
    option = True
    while option:
        n = int(input('Please input a number: '))
        if n < 1:
            print('Please add a number greater than 1 (n>1)')
        else:
            option = False
    caculate_collatz(n, steps=0)