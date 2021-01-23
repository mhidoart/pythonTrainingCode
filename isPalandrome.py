def is_palandrome(word):
    word = word.lower()
    return word[::-1] == word

def is_anagram(w1,w2):
    w1 = w1 .lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)
def dictionaryFill(string):
    dictionary = {}
    for c in string:
        if c in dictionary:
            dictionary[c]+= 1
        else:
            dictionary[c]=1
    print(dictionary)
print(is_palandrome("moim"))
print(is_anagram("iceman","cinema"))
dictionaryFill("assabbane")
