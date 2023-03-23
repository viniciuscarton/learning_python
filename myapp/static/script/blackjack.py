# there are a few issues with this code. Might come back later
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
play = True
def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    y_cards = []
    c_cards = []
    def deal_card():
        for i in range(1):
			n = random.randint(0, len(cards) - 1)
			y_cards.append(cards[n])
			del cards[n]
			n = random.randint(0, len(cards) - 1)
			c_cards.append(cards[n])
			del cards[n]
        # print(y_cards)
        # print(c_cards)
    deal_card()
    deal_card()
    print("Your cards: "), print(y_cards)
    print("Computer's first card: "), print(c_cards[0])
    # print("pc")
    # print(c_cards)
    y_cards_sum = sum(y_cards)
    c_cards_sum = sum(c_cards)
    computers_time = ""
    end_of_game = False
    # print(y_cards_sum)
    # print(c_cards_sum)
    while end_of_game is False:
        if 11 in y_cards:
            print("You win :D")
            end_of_game = True
        elif 11 in c_cards:
            print("You lose :(")
            end_of_game = True
        elif y_cards_sum > 21:
            print("You lose :(")
            end_of_game = True
        elif y_cards_sum < 21:
            another_card = input("Would user like to get another card? (Y/N): ").upper()

        if another_card == "Y":
            y_cards.append(cards[random.randint(0, len(cards) - 1)])
            y_cards_sum = sum(y_cards)
            c_cards_sum = sum(c_cards)
            print(y_cards)
            # print("user")
            # print(y_cards)
            # print(y_cards_sum)
            # print("pc")
            # print(c_cards)
            # print(c_cards_sum)
            if y_cards_sum > 21:
                print("You lose :(")
                end_of_game = True
        else:
            if c_cards_sum > y_cards_sum and c_cards_sum < 21:
                computers_time == "Please"
                print("You lose :(")
                end_of_game = True
            if computers_time == "Please" and c_cards_sum < 17:
                c_cards.append(cards[random.randint(0, len(cards) - 1)])
                y_cards_sum = sum(y_cards)
                c_cards_sum = sum(c_cards)
                # print("user")
                # print(y_cards)
                # print(y_cards_sum)
                # print("pc")
                # print(c_cards)
                # print(c_cards_sum)

            if end_of_game is not True:
                if c_cards_sum > 21:
                    print("You win :D")
                    end_of_game = True
                elif c_cards_sum > y_cards_sum:
                    print("You lose :(")
                    end_of_game = True
                elif c_cards_sum == y_cards_sum:
                    print("Draw '.'")
                    end_of_game = True
                else:
                    print("You lose :(")
                    end_of_game = True

    play = input("Would you like to play again? (Y/N): ").upper()
    if play == "Y":
        blackjack()
    else:
        play = False


blackjack()
