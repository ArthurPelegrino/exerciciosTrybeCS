import random
import json

# import csv


def vertical_name(name):
    name = input("Type a name: ")
    total = len(name)
    while total > 0:
        for letter in name:
            print(name[:total])
            total -= 1


# verticalName("arthur")

word_list = [
    "Elephant",
    "Sunshine",
    "Bicycle",
    "Whisper",
    "Rainbow",
    "Moonlight",
    "Adventure",
    "Delicious",
    "Serendipity",
    "Enchanting",
    "Harmony",
    "Radiant",
    "Wanderlust",
    "Blossom",
    "Tranquil",
    "Melody",
    "Jubilant",
    "Serenity",
    "Cascade",
    "Blissful",
]


def game_of_names():
    with open("words.txt", "r") as list_of_words:
        list_of_words = [word.strip() for word in list_of_words]
        chosen_word = random.choice(list_of_words)
        scrumbled_word = "".join(random.sample(chosen_word, len(chosen_word)))
        print(scrumbled_word)
        userAnswer = input("Type the word in the correct way: ")
        chances = 3
        while chances > 0:
            if userAnswer == chosen_word:
                print(f"Congratulations, you get it right! '{chosen_word}'")
                break
            else:
                chances -= 1
                print(
                    f"You miss a chance, try again. ({chances} chances left)"
                )
            userAnswer = input("Type the word in the correct way: ")
        if chances <= 0:
            print("You loose ):, but you can aways try again :D")
            print(f"The correct word was {chosen_word}")


# game_of_names()
