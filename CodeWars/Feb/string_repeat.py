#https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python

def repeat_str(repeat, string):
    res = ""
    for i in range(repeat):
        res += string
    return res


print(repeat_str(10,"Penrose"))

