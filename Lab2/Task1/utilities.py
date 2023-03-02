def get_list_of_sentences(text):  # (including 1 symbol sentences)
    text = text.replace('?', '.')
    text = text.replace('!', '.')
    text = text.replace('...', '.')
    list_of_sentences = text.split('. ')

    temp_list = []
    for el in list_of_sentences:
        temp_list.append(el.strip())
    list_of_sentences = temp_list

    while '' in list_of_sentences:
        list_of_sentences.remove('')

    return list_of_sentences


def get_amount_of_sentences(text):
    list_of_sentences = get_list_of_sentences(text)
    count = 0
    for el in list_of_sentences:
        if len(el) > 1 and not el[len(el) - 1].isupper():
            count += 1

    return count


def get_amount_of_non_declarative_sentences(text):
    count = text.count('!') + text.count('?')
    return count


def get_average_amount_of_words_in_sentence(text):
    list_of_sentences = get_list_of_sentences(text)
