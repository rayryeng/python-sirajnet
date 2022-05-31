"""
SirajNet: Using deep complicated NLP to turn your text into
my text by arbitrarily swapping words for their synonyms. /s

This file consists of one module function called `make_mine`. It takes
in a string as well as a "swap_rate" and will output a new string
where each word has a `1 / swap_rate` chance of being replaced
with a synonym for that word.

You can also run this file at the highest module level which
takes in command line arguments to be used with the aforementioned
function.
"""
import random
import argparse
from textblob import Word


def make_mine(yours: str, swap_rate: int) -> str:
    """
    Magic SirajNet function to use deep complicated NLP on an input
    string to transform it into a more complicated Hilbert space string
    by swapping words with their synonyms /s.

    Args:
        yours (str): The input string to transform
        swap_rate (int): The inverse of this value is the probability
                         that a word will be swapped out with a
                         corresponding synonym

    Returns:
        The newly transformed input string via SirajNet
    """
    mine = []
    for string_word in yours:
        word_object = Word(string_word)
        if random.randint(0, swap_rate - 1) == 0:
            meaning_count = len(word_object.synsets)
            if meaning_count > 0:
                meaning_selected = random.randint(0, meaning_count - 1)
                lemmas = word_object.synsets[meaning_selected].lemmas()
                synonym_count = len(lemmas)
                mine += [lemmas[random.randint(0, synonym_count - 1)].name()]
            else:
                mine += [string_word]
        else:
            mine += [string_word]

    return ' '.join(mine)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--text",
        help="Your original text",
        type=str,
        default="SaaS has dramatically lowered the intrinsic total " +\
                "cost of ownership for adopting software, solved "+\
                "scaling challenges and taken away the burden of "+\
                "issues with local hardware.")
    parser.add_argument(
        "--file",
        help="Path to text file containing text",
        type=str,
        default=None)
    parser.add_argument(
        "--chance", help="One in N swap chance", type=int, default=5)
    args = parser.parse_args()

    if args.file is None:
        your_text = args.text.split()
        MY_TEXT = make_mine(your_text, args.chance)
        print(MY_TEXT)
    else:
        with open(args.file, 'r', encoding='utf8') as f:
            for line in f:
                your_text = line.strip().split()
                MY_TEXT = make_mine(your_text, args.chance)
                print(MY_TEXT)
