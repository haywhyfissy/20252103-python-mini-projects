print("Welcome to the Love Calculator!")
print("The love score is a simple calculation based on the number of letters in the names of the two people in love.")

name_of_firstPerson = input("What is the name of the first person? ")
name_of_secondPerson = input("What is the name of the second person ")

def calculate_love_score(name1, name2):
    name = name1.lower() + name2.lower()
    true_word = calcutate_word("true",name)
    love_word = calcutate_word("love",name)
    love_score = true_word + love_word
    print (f"Your love score is {love_score}%.")


def calcutate_word(word, namez):
    letter_count = 0
    word_list = list(word)
    namez_list = list(namez)
    
    for letter in word_list:
        namez_count = namez_list.count(letter)
        letter_count += namez_count
    return str(letter_count)

calculate_love_score(name_of_firstPerson, name_of_secondPerson)

