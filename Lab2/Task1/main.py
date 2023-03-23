import utilities
f = open('text.txt')
text = f.read()

print(f'Amount of sentences: {utilities.get_amount_of_sentences(text)}')
print(f'Amount of non-declarative sentences: {utilities.get_amount_of_non_declarative_sentences(text)}')
print(f'Average amount of characters in sentences: {utilities.get_average_amount_of_characters_in_sentence(text)}')
print(f'Average amount of characters in word: {utilities.get_average_amount_of_characters_in_word(text)}')
print('Top-K N-grams:')
k = input('Input k: ')
n = input('Input n: ')
print(utilities.get_top_grams(text, k, n))
