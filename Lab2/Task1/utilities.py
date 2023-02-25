def get_amount_of_declarative_sentences(text):
    list_of_words = text.split('.')
    count = 0
    temp_list = []
    for el in list_of_words:
        temp_list.append(el.strip())
    list_of_words = temp_list
    for el in list_of_words:
        if len(el) > 1:
            count += 1
    return count
