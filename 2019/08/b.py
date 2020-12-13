print(*map(lambda r: ''.join(r).replace('0', ' '), list(zip(*[iter(list(map(
    lambda p: next(filter(lambda v: v != '2', p)), zip(*zip(*[iter(open(
        'input.txt').readline().strip())]*(25*6))))))]*25))), sep='\n')
