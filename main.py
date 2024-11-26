def find_min_energy(C,B):
    min_energy = 0
    for city in C:
        min_energy += city
    for energy in B:
        min_energy -= energy
    if min_energy <= 0:
        min_energy = C[0]
    return min(min_energy, C[0])

def find_max_city(begin, C, B):
    count = 0
    for index in range(len(C)):
        begin -= C[index]
        if begin < 0:
            break
        else:
            count += 1
            if index == len(C) - 1:
                return count
            begin += B[index]
    return count

def so_thanh_pho(A: int, C:list, B:list):
    i = 0
    while True:
        A -= C[i]
        if A < 0:
            return i
        else:
            i += 1
            A += B[i]
if __name__ == '__main__':
    begin = 10
    C = [3, 4, 5, 6]  # 4 cities to traverse
    B = [2, 1, 0]  # Replenishment only for the first 3 cities
    print(find_max_city(begin,C,B))
