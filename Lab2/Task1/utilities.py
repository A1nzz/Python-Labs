import re
import constants


def get_amount_of_sentences(text):
    match = re.findall(constants.DECLARATIVE_PATTERN, text)
    amount = len(match)
    for abbreviation in constants.TWO_WORDS_ABBREVIATIONS:
        amount -= text.count(abbreviation) * 2
    return amount


def get_amount_of_non_declarative_sentences(text):
    match = re.findall(constants.NON_DECLARATIVE_PATTERN, text)
    return len(match)


def get_words_list(text):
    nums_match = re.findall(constants.NUMBER_PATTERN, text)
    words_match = re.findall(constants.WORD_PATTERN, text)
    words = [word for word in words_match if word not in nums_match]
    return words


def get_average_amount_of_characters_in_sentence(text):
    words = get_words_list(text)
    number_of_characters = sum(len(word) for word in words)
    return number_of_characters / get_amount_of_sentences(text)


def get_average_amount_of_characters_in_word(text):
    words = get_words_list(text)
    number_of_characters = sum(len(word) for word in words)
    return number_of_characters / len(words)


def get_top_grams(text: str, k=10, n=4):
    n_grams: dict[str, int] = {}
    words = re.findall(constants.WORD_PATTERN, text.lower())  # including numbers and register does not matter
    for word_index in range(len(words) - int(n) + 1):
        n_gram = ' '.join(str(word) for word in words[word_index:word_index + int(n)])
        if n_gram in n_grams:
            n_grams[n_gram] += 1
        else:
            n_grams[n_gram] = 1
    sorted_n_grams = sorted(n_grams.items(), reverse=True, key=lambda item: item[1])
    result = sorted_n_grams[0:int(k)]
    return result
