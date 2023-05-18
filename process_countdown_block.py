
def countdown(ns):
    count = 0
    for n in ns:
        while n > 0:
            n -= 1
    return len(ns)