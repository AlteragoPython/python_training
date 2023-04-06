def custom_range(seq, *args):
    start, stop, step = (None, None, 1)

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args

    if start is not None and start not in seq:
        raise ValueError(f"{start} is not in sequence")

    index = seq.index(start) if start is not None else 0
    end_index = seq.index(stop) if stop is not None else len(seq)

    return [seq[i] for i in range(index, end_index, step)]