def reverse_words(text):
    res = ""
    for x in text.split(" "):
        res += (x[::-1] + " ")
    return res.strip()

reverse_words("This is an example!")
