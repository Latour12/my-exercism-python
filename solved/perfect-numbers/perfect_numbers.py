def classify(number):
    if number < 1:
        raise ValueError('Number must be strictly positive')
    dividers = [i for i in range(1,number) if number % i == 0]
    if sum(dividers) == number:
        return 'perfect'
    elif sum(dividers) > number:
        return 'abundant'
    elif sum(dividers) < number:
        return 'deficient'
