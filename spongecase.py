#a style of text where letters alternately appear in lower and upper case starting with lowercase
def sponge_upper(my_str):
    lst = list(my_str)
    index = 0
    for i in range(len(lst)):
        #use a flag is the only way ):)
        index += 1
        if lst[index].isalpha() and index % 2 == 1:
            lst[index] = lst[index].upper()
        elif lst[index] == ' ':
            index += 1
    return "".join(lst)

print(sponge_upper("hello world"))