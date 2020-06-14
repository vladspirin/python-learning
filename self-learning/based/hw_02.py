def get_percentage(number, ndigits=None):
    result = round((float(number) * 100), ndigits)
    return print(f'{result}%')

get_percentage(0.0123)