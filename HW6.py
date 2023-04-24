def merge_elems(*elems):
    for elem in elems:
        if isinstance(elem, str) or not hasattr(elem, '__iter__'):
            yield elem
        else:
            yield from merge_elems(*elem)

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