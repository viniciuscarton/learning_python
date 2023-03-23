import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program!")
total_bids = {}
again = "Y"

while again == "Y":
    name = input("What is your name? ").upper()
    bid = input("What is your bid? $")
    total_bids[name] = bid
    os.system('cls')
    again = input("Another (Y/N)? ").upper()


winning_bid = max(total_bids.values(), key=int)
winner = ""

for key, value in total_bids.items():
    if value == winning_bid:
        winner = key

print(f"The winner is {winner} with a bid of ${winning_bid}")
