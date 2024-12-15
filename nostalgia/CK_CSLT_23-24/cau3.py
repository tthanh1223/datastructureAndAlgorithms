# l_i là các độ dài của các từ trong câu và w_i là số từ có độ dài l_i trong câu.
# tính trọng số của của.
# input: 1 string
# output: trọng số

def calculate_the_mean(string: str):
    count_length = {}
    # dung sliding window ne
    words = string.split(' ')
    for word in words:
        count_length[len(word)] = count_length.get(len(word), 0) + 1
    norm = 0
    denorm = 0
    for i in count_length:
        norm += i * count_length[i]
        denorm += i
    return norm/denorm

if __name__ == "__main__":
    a = calculate_the_mean(input())
    print(a)