import string
import random

phrase = "viet nam khong can xuong mau viet nam keu goi thuong nhau viet nam"
def create_random_phrase() -> string:
    """Generate a random phrase of length 27."""
    return ''.join(random.choices((string.ascii_lowercase+' '), k = len(phrase)))

#This function compares the randomly generated string to the target phrase.
# It should return a score that indicates how many characters are correct in the generated string.
def score(candidate: str) -> int:
    return sum(1 for i, c in enumerate(candidate) if c == phrase[i])


#keeping the right letter
def keeping_letter(base:str):
    #select a random position to change
    index = random.randint(0, len(base)-1)
    #Create a new character
    new_char = random.choice(string.ascii_lowercase+' ')
    while new_char == base[index]:
        new_char = random.choice(string.ascii_lowercase+' ')
    new_check_phrase = base[:index] + new_char + base[index+1:]
    return new_check_phrase

def main():
    highest_score = 0
    best_phrase = create_random_phrase()
    count = 0
    while highest_score < len(phrase):
        new_phrase = keeping_letter(best_phrase)
        phrase_score = score(new_phrase)

        if phrase_score > highest_score:
            highest_score = phrase_score
            best_phrase = new_phrase

        print(best_phrase, highest_score)
        count += 1

    print(best_phrase, highest_score,count)
main()
