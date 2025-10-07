import random

def shoot_ball():
    # 50% chance to make the shot
    return random.choice([True, False])

def basketball_game():
    score = 0
    shots = 5
    print("Welcome to the Basketball Shooting Game!\n")
    for i in range(shots):
        input(f"Press Enter to shoot ball {i+1}...")
        if shoot_ball():
            print("Nice shot! You scored 2 points.")
            score += 2
        else:
            print("Missed the shot!")
    print(f"\nGame Over! Your total score: {score}")

if __name__ == "__main__":
    basketball_game()