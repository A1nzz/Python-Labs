def get_amount_of_sentences(text):
    text = text.replace('?', '.')
    text = text.replace('!', '.')
    list_of_sentences = text.split('.')
    temp_list = []

    for el in list_of_sentences:
        temp_list.append(el.strip())

    list_of_sentences = temp_list
    count = 0
    for el in list_of_sentences:
        if len(el) > 1:
            count += 1

    return count


def get_amount_of_non_declarative_sentences(text):
    count = text.count('!') + text.count('?')
    return count
