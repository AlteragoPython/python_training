from collections import Counter


def major_and_minor_elem(inp: list) -> tuple[int, int]:
    counter_list = Counter(inp)
    most_common = counter_list.most_common(1)
    least_common = counter_list.most_common()[:-2:-1]
    result = (most_common[0][0], least_common[0][0])
    print(result)

list1 = [2,2,1,1,1,2,2,3,3,3,3,3]
major_and_minor_elem(list1)
