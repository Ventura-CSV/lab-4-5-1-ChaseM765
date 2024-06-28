import random


def main():
    import random
    x = 0
    total = 0
    numbers = []
    for x in range (0,5):
        ran = random.randint(0,100)
        numbers.append(ran)
        total += ran

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
