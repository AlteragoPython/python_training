def custom_range(seq, start, stop=None, step=1):
    if stop is None:
        stop = start
        start = seq[0]
    index_start = seq.index(start)
    if step > 0:
        index_stop = len(seq) if stop is None else seq.index(stop)
    else:
        index_stop = seq.index(stop) - 1 if stop is not None else -1
    return list(seq[index_start:index_stop:step])