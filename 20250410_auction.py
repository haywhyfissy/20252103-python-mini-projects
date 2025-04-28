bid = {}
print ("Welcome to the secret auction program.")

continue_bidding = True
while continue_bidding:
    bidder = input("Enter your name: ").lower()
    bid_amount = int(input("Enter your bid amount: $"))
    bid[bidder] = bid_amount

    more_bidders = input("Are there any other bidders? Type 'y'or 'yes' or 'no' or 'n': ").lower()

    if more_bidders == "no" or more_bidders == "n":
        continue_bidding = False
       
    elif more_bidders == "yes" or more_bidders == "y":
        print("\n" * 100)
    
    
print("The bidding has ended.")
winner = ""
highest_bid = 0
for bidder in bid:
    bid_amount = bid[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The highest bidder is {winner} with ${highest_bid}")
print(bid)
