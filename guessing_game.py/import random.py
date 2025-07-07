import random
import os
import time

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Step 1: Setup players
num_players = input("👥 How many players? ").strip()

while not num_players.isdigit() or int(num_players) < 1:
    num_players = input("❗ Please enter a valid number of players (1 or more): ").strip()

num_players = int(num_players)
players = {}

for i in range(1, num_players + 1):
    name = input(f"Enter name for Player {i}: ").strip().title()
    players[name] = {'wins': 0, 'losses': 0}

# Step 2: Main game loop (rounds)
while True:
    clear_screen()
    print("\n🎯 Current Standings:")
    for p, stats in players.items():
        print(f"{p} ➔ Wins: {stats['wins']} | Losses: {stats['losses']}")

    # Each player takes their turn in this round
    for player_name in players:
        print(f"\n👉 Now it’s {player_name}'s turn!")
        print(f"Score ➔ Wins: {players[player_name]['wins']} | Losses: {players[player_name]['losses']}")

        number_to_guess = random.randint(1, 10)
        attempts = 3
        previous_guesses = []

        print("\nI'm thinking of a number between 1 and 10.")

        while attempts > 0:
            guess = input("Take a guess: ")

            if not guess.isdigit():
                print("❗ Please enter a valid number.")
                continue

            guess = int(guess)

            if guess < 1 or guess > 10:
                print("❗ Invalid guess. Please enter a number between 1 and 10.")
                continue

            if guess in previous_guesses:
                print("❗ You've already guessed that number. Try again.")
                continue

            previous_guesses.append(guess)

            if guess == number_to_guess:
                print(f"🎉 Congratulations, {player_name}! You guessed it right!")
                players[player_name]['wins'] += 1
                break
            else:
                attempts -= 1
                print(f"❌ Wrong guess. You have {attempts} attempts left.")

        if attempts == 0:
            print(f"😞 Sorry, {player_name}, you're out of attempts. The number was {number_to_guess}.")
            players[player_name]['losses'] += 1

        print(f"\n🔢 {player_name}'s Score ➔ Wins: {players[player_name]['wins']} | Losses: {players[player_name]['losses']}")

        # ✅ Automatic brief pause so player sees result
        time.sleep(2)

        # Assess the current winner(s) so far
        max_wins = max(stats['wins'] for stats in players.values())
        leaders = [p for p, stats in players.items() if stats['wins'] == max_wins]

        if max_wins == 0:
            print("\n🕹 No one has won any rounds yet!")
        elif len(leaders) == 1:
            print(f"\n🏅 Current leader: {leaders[0]} with {max_wins} win{'s' if max_wins > 1 else ''}.")
        else:
            leaders_list = ', '.join(leaders)
            print(f"\n🤝 It's currently a tie between: {leaders_list} with {max_wins} win{'s' if max_wins > 1 else ''} each.")


    # Step 3: End of round—ask if players want another round or to quit
    while True:
        next_round = input("\nWould you like to play another round? (Y/N): ").strip().lower()
        if next_round in ['y', 'n']:
            break
        print("❗ Please enter Y or N.")

    if next_round == 'n':
        clear_screen()
        print("\n🏁 Final Scores:")
        for p, stats in players.items():
            print(f"{p} ➔ Wins: {stats['wins']} | Losses: {stats['losses']}")

        max_wins = max(stats['wins'] for stats in players.values())
        winners = [p for p, stats in players.items() if stats['wins'] == max_wins]

        if max_wins == 0:
            print("\nNo one won any games this time!")
        elif len(winners) == 1:
            print(f"\n🏆 The winner is {winners[0]} with {max_wins} wins!")
        else:
            winners_list = ', '.join(winners)
            print(f"\n🤝 It's a tie between: {winners_list} with {max_wins} wins each!")

        print("\n👋 Thanks for playing!")
        break

                      
                      
        

