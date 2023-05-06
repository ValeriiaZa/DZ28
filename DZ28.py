def prime_generator(end):
    for i in range(2, end):
        for k in range(2, i+1):
            if i == 2:
                yield i
                break
            elif i % k == 0:
                break
            elif i != (k+1):
                continue
            else:
                yield i
                break
