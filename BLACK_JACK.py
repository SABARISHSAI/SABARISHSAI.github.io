import random
from art import logo
new_game = True
while new_game:
    choice = input("Do you want to play a game of blackjack? type y or n : ").lower()
    if choice == 'n':
        break
    else:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        def generate_card():
            card_number = random.choice(cards)
            return card_number
        if choice == 'y':
            print("\n"*100)
            print(logo)
            card_1 = random.choice(cards)
            card_2 = random.choice(cards)
            user_cards=[card_1,card_2]
            current_Score = card_1+card_2
            print(f"      your cards: {user_cards}, current score: {current_Score}")
            computer_card1 = random.choice(cards)
            computer_card2 = random.choice(cards)
            computer_card = [computer_card1, computer_card2]
            print(f"      computer's first card: {computer_card1}")
            game = True

            while game==True and current_Score<21:
                choose = input("type y to get another card otherwise n : ")
                if choose == 'y':
                    card = generate_card()
                    user_cards.append(card)
                    current_Score = sum(user_cards)
                    print(f"      your cards: {user_cards}, current score: {current_Score}")
                if choose == 'n':
                    game = False
                    if current_Score > sum(computer_card) and current_Score<21:
                        print(f"      your cards: {user_cards}, current score: {current_Score}")
                        print(f"      computer's final hand: {computer_card}, final_score: {sum(computer_card)}")
                        print("You Won")
                    if current_Score < sum(computer_card) and sum(computer_card)<21:
                        print(f"      your cards: {user_cards}, current score: {current_Score}")
                        print(f"      computer's final hand: {computer_card}, final_score: {sum(computer_card)}")
                        print("You went over. You lose 😭")
                    if current_Score == sum(computer_card):
                        print("DRAW : you and computer got same score, ")
            if current_Score>21:
                print(f"computer's final hand: [{computer_card1}], final_score: {computer_card1}")
                print("You went over. You lose 😭")

            if current_Score==21:
                print("You win 😃")
            if sum(computer_card)==21:
                print(f"computer's final hand: {computer_card}, final_score: {sum(computer_card)}")
                print("computer won")






