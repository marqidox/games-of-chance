import random

money = 100

def coin_flip(bet):
    print('Playing coin flip!')
    if bet > 0 and bet < money:
        coin_flip_result = random.randint(0,1)
        outcome = None 
        call = input('Pick a side!')
        call = call.lower().title()
        if call == 'Heads' or call == 'Tails':
            if coin_flip_result == 0:
                outcome = 'Heads'
                print(outcome)
            else:
                outcome = 'Tails'
                print(outcome)
    
            if outcome == call:
                print(f'You won! You earn {bet} dollars!')
                return bet
            else:
                print(f'You lost! You lose {bet} dollars!')
                return bet * -1
        else:
            print('Enter heads or tails!')
    else:
        print('Enter a postive number/enter within the range of your money!')

def cho_han(bet):
    print('Playing cho_han!')
    if bet > 0 and bet < money:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = (dice1 + dice2) % 2
        call = input('Choose even or odd!')
        call = call.lower().title()
        if call == 'Even' or call == 'Odd':
            if total == 0:
                outcome = 'Even'
                print(outcome)
            else:
                outcome = 'Odd'
                print(outcome)
    
            if outcome == call:
                print(f'You won! You earn {bet} dollars!')
                return bet
            else:
                print(f'You lost! You lose {bet} dollars!')
                return bet * -1
        else:
            print('Enter even or odd!')
    else:
        print('Enter a postive number/enter within the range of your money!')

def pick_a_card(bet):
    print('Playing pick a card!')
    if bet > 0 and bet < money:
        card_deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        player_call = random.randint(0, len(card_deck)-1)
        computer_call = random.randint(0, len(card_deck)-1)

        player_choice = card_deck[player_call]
        print(f'You picked the card: {player_choice}')
        computer_choice = card_deck[computer_call]
        print(f'Player2 picked the card: {computer_choice}')
        if player_choice == 'Ace':
            player_choice = 1
        elif player_choice == 'Jack' or player_choice == 'Queen' or player_choice == 'King':
            player_choice = 10

        if computer_choice == 'Ace':
            computer_choice = 1
        elif computer_choice == 'Jack' or computer_choice == 'Queen' or computer_choice == 'King':
            computer_choice = 10

        if player_choice > computer_choice:
            print(f'You won! You earn {bet} dollars.')
            return bet
        elif computer_choice > player_choice:
            print(f'You lost! You lose {bet} dollars.')
            return bet * -1
        elif player_choice == computer_choice:
            print('A tie! You neither lose nor earn anything.')
            return 0
    else:
        print('Enter a postive number/enter within the range of your money!')

def roulette(bet):
    print('Playing roulette!')
    if bet > 0 and bet < money:
        what_bet = input('What would you like to bet on? Choose: color, parity, or number.')
        what_bet = what_bet.lower()
        call = None
        if what_bet == 'color':
            call = input('Pick red or black!')
            call = call.lower().title()
        if what_bet == 'number':
            call = input('Pick a number from 1 to 37.')  
        if what_bet == 'parity':
            call = input('Pick odd or even!') 
            call = call.lower().title()
        even_or_odd = lambda num: 'Even' if num%2==0 else 'Odd'
        red_or_black = lambda num: 'Red' if num in red_numbers else 'Black'
        nums = range(1, 37)
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        spin_dict = {}
        for num in nums:
            spin_dict[num] = even_or_odd(num), red_or_black(num)
        key = random.choice(list(spin_dict.keys()))
        b, c = spin_dict.get(key)
        spin = f'{key} {b, c}'
        print(spin)

        if type(call) != int:
            if call in spin:
                print(f'You won! You earn {bet} dollars.')
                return bet
            else:
                print(f'You lost! You lose {bet} dollars.')
                return bet * -1
        else:
            if call in spin:
                print(f'You won! You earn {bet * 35} dollars.')
                return bet * 35
            else:
                print(f'You lost! You lose {bet} dollars.')
                return bet * -1
    else:
        print('Enter a positive number/enter within the range of your money!')

def play_game():
    pick_a_game = input('What game would you like to play: coin flip, pick a card, cho han, or roulette?')
    pick_a_game = pick_a_game.lower()
    if pick_a_game == 'coin flip':
        bet = int(input('Bet money!'))
        money += coin_flip(bet)
        print(f'Your current money is {money}')
    if pick_a_game == 'cho han':
        bet = int(input('Bet money!'))
        money += cho_han(bet)
        print(f'Your current money is {money}')
    if pick_a_game == 'pick a card':
        bet = int(input('Bet money!'))
        money += pick_a_card(bet)
        print(f'Your current money is {money}')
    if pick_a_game == 'roulette':
        bet = int(input('Bet money!'))
        money += roulette(bet)
        print(f'Your current money is {money}')

play_game()