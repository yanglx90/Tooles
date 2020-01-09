import math


def step(a, b):
    print('', '%', end='\r', flush=True, )
    if a < b - 1:
        print('\033[30;36m', '>' * math.ceil(a / b * 100), ' ' * math.ceil((b - a) / b * 100), '|',
              round(a / b * 100, 2), '%', end='\033[0m', flush=True, )
    else:
        print('\033[30;36m', '>' * math.ceil(a / b * 100), '  |' + '100.00', '%\033[0m', flush=True, )