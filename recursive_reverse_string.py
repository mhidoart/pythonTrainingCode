def reverse(word,res=""):
    if len(word)==0:
        return res
    else:
        res += word[-1]
        return reverse(word[:-1],res)
print(reverse("assabbane"))
