from art import logo

print("Welcome to Auction")
print(logo)
bids = {}

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount Rs:{highest_bid}")


continue_bidding = True
while continue_bidding:
    name = input("What name you want enter:\n").lower()
    bid_price = int(input("What is the bid price ?\nRs: "))
    bids[name] = bid_price
    should_continue = input("Ask if there are any other user ? 'yes' or 'no' \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" *1000)




