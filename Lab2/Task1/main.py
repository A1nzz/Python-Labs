import utilities

text = "There are p.m. usually about 200 words in a paragraph, " \
       "but this can vary widely... Most paragraphs focus on a " \
       "single idea that's expressed with an introductory sentence, " \
       "then followed by two or more supporting sentences about the idea. " \
       "A short paragraph may not reach even 50 words" \
       " while long paragraphs can be over 400 words long," \
       " but generally speaking they tend to be approximately 200 words in length."

print(utilities.get_amount_of_sentences(text))
print(utilities.get_amount_of_non_declarative_sentences(text))
print(utilities.get_average_amount_of_characters_in_sentence(text))
print(utilities.get_average_amount_of_characters_in_word(text))
print(utilities.get_top_grams(text, 1, 1))
