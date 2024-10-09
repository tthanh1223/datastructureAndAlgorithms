digits = [1,2,3,4,5]
result = []
number = str()
for i in digits:
    number += str(i)
number = int(number) +1
for i in str(number):
    result.append(int(i))
print(result)