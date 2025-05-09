import random

your_cards = []
dealer_cards = []
stack_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K', 'A']




print(""""
    Welcome to Blackjack!\n
    You will be playing against the dealer\n
    The goal is to get as close to 21 as possible without going over\n
    The dealer must hit until they reach 17 or higher\n
    """)


def blackjack(your_cards, dealer_cards):
    your_total = 0
    dealer_total = 0
    for your_card_num in your_cards:
        your_total += your_card_num
        if your_total > 21:
            print(f"Oops, You loose!!!\n You have a total of {your_total} while the Dealer has {dealer_total}")
            break
    for dealer_card_num in dealer_cards:
        dealer_total += dealer_card_num
        if dealer_total > 21:
            print(f"Congratulations, You win!!!\n You have a total of {your_total} while the Dealer has {dealer_total}")
            break
    if your_total == dealer_total:
        print(f"The game ends in a Draw!!!\n You and the dealer have the same total score of {your_total}")
    elif your_total > dealer_total:
        print(f"Congratulations, You win!!!\n You have a total of {your_total} while the Dealer has {dealer_total}")
    else:
        print(f"Oops, You loose!!!\n You have a total of {your_total} while the Dealer has {dealer_total}")

def pick_card():
    card = random.choice(stack_of_cards)
    stack_of_cards.remove(card)
    return card


choose_card = input("Do you want to pick another card: y/n").lower()

if choose_card == 'y':
    your_new_card = pick_card()
    your_cards.append(your_new_card)
    print(f"You chose {your_new_card}, Your available cards: {your_cards}, Current score: {sum(your_cards)}")
    dealer_new_card = pick_card()
    dealer_cards.append(dealer_new_card)
    print (f"The dealer chose: {dealer_new_card}")
elif choose_card == 'n':
    print("You have chosen not to pick another card.")
    blackjack(your_cards, dealer_cards)

else:
    print("Invalid input. Please enter 'y' or 'n'.")
    choose_card = input("Do you want to pick another card: y/n").lower()










def card_number(card, ):
    if card in stack_of_cards:
        
        
        
        if card in ['Q', 'J', 'K']:
            return 10
        elif card == 'A':
            # Ace can be 1 or 11
            num_A = int(input("Do you want Ace to be 1 or 11? (1/11): "))
            if num_A == 1:
                return 1
            elif num_A == 11:
                return 11
            else:
                print("Invalid input. Ace will be counted as 11.")
            return 11
    elif card 
    
    else:
        return card
    
