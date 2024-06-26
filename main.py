from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finish = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_reccord = {amit:200, rajni:900}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of {highest_bid}")

while not bidding_finish:
    name = input("Enter your name: ")
    Price = int(input("Enter you Bid?: $"))
    bids[name] = Price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
