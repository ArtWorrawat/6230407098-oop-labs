directory = {"manee":"1234", "mana":"4567", "chujai":"6789"}

item = set(directory.items())
list_item = list(item)
print(list_item)

val = list(directory.values())
print(val)

key = list(directory.keys())
print(key)

word = "antidisestablishmentarianism"
word = list(word)
word.sort()
word = "".join(word)
print(word)

sentence = "the quick brown fox jumped over the lazy dog"
print(sentence.split())



