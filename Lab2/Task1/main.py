import utilities


if __name__ == "__main__":
    f = open('text.txt')
    text = f.read()
    print(f'Amount of sentences: {utilities.get_amount_of_sentences(text)}')
    print(f'Amount of non-declarative sentences: {utilities.get_amount_of_non_declarative_sentences(text)}')
    print(f'Average amount of characters in sentences: {utilities.get_average_amount_of_characters_in_sentence(text)}')
    print(f'Average amount of characters in word: {utilities.get_average_amount_of_characters_in_word(text)}')
    print('Top-K N-grams:')
    while True:
        try:
            k = int(input('Input k: '))
            break
        except ValueError:
            print("Incorrect input! Try again: ")
    while True:
        try:
            n = int(input('Input n: '))
            break
        except ValueError:
            print("Incorrect input! Try again: ")

    print(utilities.get_top_grams(text, k, n))

