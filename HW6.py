def merge_elems(*elems):
    for el in elems:
        if isinstance(el, str) and len(el) > 1:
            for char in el:
                yield char
        elif isinstance(el, (list, tuple)):
            for item in el:
                yield from merge_elems(item)
        else:
            yield el

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')



def map_like(fun, *elems):
    for elem in elems:
        try:
            result = fun(elem)
        except Exception as e:
            result = f"{elem}: {str(e)}"
        yield result

a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

for _ in map_like(fun, a, b, c, d):
    print(_)