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

