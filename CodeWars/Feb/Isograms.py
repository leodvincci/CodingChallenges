#https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

"""

    #create a map/dictionary
    #iterate over string and put chars in dictionary
        - {
            char:cnt,
            char:cnt,
            char:cnt
            }
    
        - if char aready in diction
            --return false
    return true at end of iteration
"""

def is_isogram(string):
    myMap = {}
    for c in string.lower():
        if myMap.get(c) == 1:
            print(False)
            return False
        else:
            myMap[c] = 1
    print(True)
    return True
    
def is_isogram_2(string):
   
    for c in string:
        print(string.lower().count(c))
        if string.lower().count(c) > 1:
            print(False)
            return False
    print(True)
    return True





# is_isogram("qxcFKtHqRdiyUIDLrTzPgXuXWKYsM")
# is_isogram("Dermatoglyphics")
# is_isogram("aba")
# is_isogram("moOse")
# is_isogram("isIsogram")
# is_isogram("")


# is_isogram_2("qxcFKtHqRdiyUIDLrTzPgXuXWKYsM")
# is_isogram_2("Dermatoglyphics")
# is_isogram_2("aba")
# is_isogram_2("moOse")
# is_isogram_2("isIsogram")
# is_isogram_2("")