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


# def get_average_amount_of_characters_in_sentence(text):
#     list_of_sentences = get_list_of_sentences(text)
#     sentences_count = len(list_of_sentences)
#     symbols_count = 0
#     for sentence in list_of_sentences:
#         list_of_words = sentence.split()
#         for word in list_of_words:
#             if word.isdigit():
#                 continue
#             symbols_count += len(word)
#     return symbols_count / sentences_count


# def get_average_amount_of_characters_in_words(text):
#     symbols_count = 0
#     words_count = 0
#     list_of_sentences = get_list_of_sentences(text)
#     for sentence in list_of_sentences:
#         list_of_words = sentence.split()
#         for word in list_of_words:
#             if word.isdigit():
#                 continue
#             symbols_count += len(word)
#             words_count += 1
#     return symbols_count / words_count
