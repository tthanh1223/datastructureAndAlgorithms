def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
    print("moving disk from",from_pole,"to",to_pole)

move_tower(3, 'A', 'B', 'C')

# A    B    C
# 321
# 3    1    2
# 3         21
#      3    21
# 1    32
#      321