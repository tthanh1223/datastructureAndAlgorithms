def flatten_nested_list(nested_list):
    res = []
    for i in nested_list:
        if isinstance(i, list):
            res.extend(flatten_nested_list(i))
        else:
            res.append(i)
    return res

def flatten_nested_list2(nested_list):
    stack = [nested_list]
    flat = []
    while stack:
        b = stack.pop(0)
        if isinstance(b, list):
            stack = b + stack
        else:
            flat.append(b)
    return flat


a = [1, [2, [4, 5], 3]]
print(flatten_nested_list2(a))