def count_brother(string: str, k:int):
    lower_dict = {}
    upper_dict = {}
    count = 0
    # Make count dict
    for i in range(len(string)):
        if string[i].islower():
            lower_dict[string[i]] = lower_dict.get(string[i], 0) + 1
        else:
            upper_dict[string[i]] = upper_dict.get(string[i], 0) + 1

    # Count available pair
    for i in lower_dict.keys():
        if i.upper() in upper_dict.keys():
            step = min(upper_dict.get(i.upper()), lower_dict[i])
            lower_dict[i] = lower_dict[i] - step
            upper_dict[i.upper()] = upper_dict.get(i.upper()) - step
            count += step

    # Make the change and count
    while k >= 0:
        for char in lower_dict.keys():
            if upper_dict.get(char.upper(),0) == 0 and lower_dict[char] >= 2:
                count += 1
                lower_dict[char] -= 2
        for char in upper_dict.keys():
            if lower_dict.get(char.lower(),0) == 0 and upper_dict[char] >= 2:
                count += 1
                upper_dict[char] -= 2
        k -= 1
    return count



if __name__ == '__main__':
    s = 'AAAAAaaaA'
    k = 2
    print(count_brother(s, k))