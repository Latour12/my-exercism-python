def steps(number):
    if number < 1:
        raise ValueError("Given number should be positive")
    step = 0
    while number != 1:
        update = 0
        if number % 2 == 0:
            update = number / 2
        else:
            update = (number * 3) + 1
        number = update
        step += 1
    return step 