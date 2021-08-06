def is_armstrong_number(number):
    total = 0
    is_armstrong_number = False
    for digit in str(number):
        total += int(digit)**len(str(number))
    if total == number:
        is_armstrong_number =True
    return is_armstrong_number
