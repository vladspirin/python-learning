from copy import deepcopy


def solve(obj):
    deep_copy = deepcopy(obj)
    return True if id(deep_copy) in any(id(obj)) else False


print(solve(1))