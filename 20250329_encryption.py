alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(en_text, en_shift):
    en_word_list = list(en_text.split())
    encryted_word_list = []

    for word in en_word_list:
        en_text_list = list(word)
        encryted_text_list = []
   
            
        for letter in en_text_list:
            if letter in alphabets:
                letter_index = alphabets.index(letter)
                new_letter_index = letter_index + en_shift
                new_letter_index = new_letter_index % len(alphabets)

                new_letter = alphabets[new_letter_index]
                encryted_text_list.append(new_letter)
        encrypted_text = "".join(encryted_text_list)            
        
        encryted_word_list.append(encrypted_text)
    
    encrypted_word = " ".join(encryted_word_list)
    print(encrypted_word)



def decrypt(de_text, de_shift):
    de_word_list = list(de_text.split())
    decrypted_word_list = []

    for de_word in de_word_list:
        de_text_list = list(de_word)
        decrypted_text_list = []
   
            
        for de_letter in de_text_list:
            if de_letter in alphabets:
                de_letter_index = alphabets.index(de_letter)
                de_new_letter_index = de_letter_index - de_shift
                de_new_letter_index = de_new_letter_index % len(alphabets)
                de_new_letter = alphabets[de_new_letter_index]
                decrypted_text_list.append(de_new_letter)
        decrypted_text = "".join(decrypted_text_list)            
        
        decrypted_word_list.append(decrypted_text)
    
    decrypted_word = " ".join(decrypted_word_list)
    print(decrypted_word)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid input")

restart = input("Do you want to continue? Type 'yes' or 'no': ").lower()
while restart == "yes":
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
else:
    print("Goodbye")
    exit()


