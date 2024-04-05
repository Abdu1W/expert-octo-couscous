import random

def start_game():
    print("Welcome to the Treasure Hunt of Despair.")
    print("Find the treasure and win. But beware, the paths are treacherous.")
    
    while True:
        choice = input("You're at a crossroad. Do you want to go left or right? ").lower()
        if choice not in ['left', 'right']:
            print("Confusing instructions appear: Try choosing an actual direction, or maybe not.")
            continue

        # Random failure condition
        if random.choice([True, False]):
            print("For no apparent reason, a boulder falls and you have to start over.")
            continue

        print(f"You decided to go {choice}. And you find a... wait for it... dead end. Game over.")
        if input("Restart the game? (yes/no): ").lower() != 'yes':
            print("Thanks for playing the Treasure Hunt of Despair. Better luck next time!")
            break

start_game()
