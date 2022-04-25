import string
import re

def make_dict_from_text(text):
    """Gets text and returns a dictionary of words
    :param text: a long text
    :return: A dictionary that contains all the words that are in the text and the number of times they have appeared
    """
    list_of_words = []
    list_ = re.split(', |:|\.|\?', text.lower())
    list_of_words_with_signs= " ".join(list_ ).split(" ")
    Net_words =(i for i in list_of_words_with_signs if i.isalpha())
    for word in Net_words:
        list_of_words.append(word)

    dict_of_word = {i:len(i) for i in list_of_words}
    return dict_of_word


if __name__ == "__main__":
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(make_dict_from_text(text))