from typing import Any, List
def combinations(*args: List[Any]) -> List[List]:
    if len(args) == 1:
        return [[i] for i in args[0]]
    else:
        result = []
        for item in args[0]:
            for sub_combination in combinations(*args[1:]):
                result.append([item] + sub_combination)
        return result
result = combinations([1, 2], [3, 4], [5, 6])
print(result)