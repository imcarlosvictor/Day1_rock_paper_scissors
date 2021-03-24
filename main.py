import random

round: int = 1
ai_wins = 0
player_wins = 0
ai_ans: str = ''
player_ans: str = ''

choices = {
    'rock': {
        'rock': 'tie',
        'paper': 'win',
        'scissors': 'lose'
    },
    'paper': {
        'rock': 'win',
        'paper': 'tie',
        'scissors': 'lose'
    },
    'scissors': {
        'rock': 'lose',
        'paper': 'win',
        'scissors': 'tie'
    }
}

player_name = input('Enter your name: ')
print('\n')

game_running = True
while game_running:

    # AI input
    ai_input: int = random.randint(0, 2)

    if ai_input == 0:
        ai_ans = 'rock'
    elif ai_input == 1:
        ai_ans = 'paper'
    elif ai_input == 2:
        ai_ans = 'scissors'

    # User input
    find_user_input = True
    while find_user_input:

        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        player_input: int = int(input("Enter the number you desire: "))

        if player_input in [1, 2, 3]:
            find_user_input = False
        else:
            print('Enter a number between 1 to 3.')
            print('\n')

    # Assign player's answer
    if player_input == 1:
        player_ans = 'rock'
    elif player_input == 2:
        player_ans = 'paper'
    elif player_input == 3:
        player_and = 'scissors'

    # Determine round winner
    round_winner: str = 'Tie'

    round_result: str = choices[player_ans][ai_ans]  # Finds the result

    # Updates round_winner and keeps track of match result
    if round_result == 'win':
        round_winner = player_name
        player_wins += 1
    elif round_result == 'lost':
        round_winner = 'AI'
        ai_wins += 1

    # Print round outcome
    print('\n')
    print('---------------------')
    print(f'{player_name}: {player_wins} | AI: {ai_wins}')
    print('---------------------')
    print(f'Round {round} Result: {round_winner}')
    print(f'{player_name} chose {player_ans}')
    print(f'AI chose {ai_ans}')
    print('---------------------')
    print('\n')

    # Keeps track of rounds
    round += 1

    # Ask whether player wants to continue every 10 rounds
    if round == 11 or round == 21:

        play_again = True
        while play_again:

            new_round = input('Would you like to continue? (y or n): ')

            if new_round == 'n':

                # Determine game winner
                if player_wins > ai_wins:
                    print(f'{player_name} wins!!')
                elif player_wins < ai_wins:
                    print('The AI wins!!')
                else:
                    print('Draw!')

                # Print Results
                print('------------------')
                print('Game Results')
                print(f'{player_name}: {player_wins} | AI: {ai_wins}')
                print('\n')
                print(f'Thanks for playing {player_name}')

                # Exit game
                play_again = False
                game_running = False
            elif new_round == 'y':
                print('\n')
                break
            else:
                print('"y" for Yes and "n" for No')
                print('\n')
