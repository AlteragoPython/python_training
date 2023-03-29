import string
def sequence(seq, start, stop=None, step=1):
    if stop is None:
        stop = seq.index(start)
        start = 0
    else:
        start = seq.index(start)
        stop = seq.index(stop)
    return [seq[i] for i in range(start, stop, step)]
