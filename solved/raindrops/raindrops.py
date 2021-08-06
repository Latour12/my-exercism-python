def convert(number):
    base = {3: 'Pling', 5: 'Plang', 7:'Plong'}
    return ''.join(drop for divisor, drop in base.items() if number % divisor == 0) or str(number)

