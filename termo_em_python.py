import random

words = [
    "python", "java", "javascript", "html", "css",
    "ruby", "php", "c++", "c#", "swift"
]

hard_games_played = 0
normal_games_played = 0
easy_games_played = 0
won_games = 0
lost_games = 0


def gameplay(hard_games_played, normal_games_played, easy_games_played,
             won_games, lost_games):

    difficulty = input(
        "What difficulty do you want to play?\n"
        "H - Hard\n"
        "N - Normal\n"
        "E - Easy\n> "
    ).upper()

    if difficulty == "H":
        chances = 3
        hard_games_played += 1

    elif difficulty == "N":
        chances = 5
        normal_games_played += 1

    elif difficulty == "E":
        chances = 7
        easy_games_played += 1

    else:
        print("Invalid input. Please choose H, N or E.")
        return hard_games_played, normal_games_played, easy_games_played, won_games, lost_games

    word = random.choice(words)

    print(f"\nThe word has {len(word)} letters.")

    for i in range(chances):
        guess = input("Try to guess the word: ").lower()

        if guess == word:
            print("Congratulations! You guessed the word!")
            won_games += 1
            break
        else:
            print(f"Wrong guess! {chances - i - 1} chances left.")

    else:
        print(f"\nYou lost! The word was '{word}'.")
        lost_games += 1

    return hard_games_played, normal_games_played, easy_games_played, won_games, lost_games


while True:

    hard_games_played, normal_games_played, easy_games_played, won_games, lost_games = gameplay(
        hard_games_played,
        normal_games_played,
        easy_games_played,
        won_games,
        lost_games
    )

    keep_playing = input("\nDo you want to play again? (Y/N): ").lower()

    if keep_playing != "y":
        break

print("\n========== GAME STATS ==========")
print(f"Games won: {won_games}")
print(f"Games lost: {lost_games}")
print(f"Hard games played: {hard_games_played}")
print(f"Normal games played: {normal_games_played}")
print(f"Easy games played: {easy_games_played}")
print("Thanks for playing!")