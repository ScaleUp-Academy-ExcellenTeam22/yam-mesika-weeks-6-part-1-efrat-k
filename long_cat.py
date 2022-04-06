import string
import re
text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

list_of_word=[]
list_=re.split(', |:|\.|\?', text.lower())
list_of_word1 =" ".join(list_).split(" ")
words =(i for i in list_of_word1 if i.isalpha())
for x in words:
    list_of_word.append(x)


dict_of_word = {i:len(i) for i in list_of_word}
print(dict_of_word)
