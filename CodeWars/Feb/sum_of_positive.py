#https://www.codewars.com/kata/5715eaedb436cf5606000381

some_arr = [1,-4,7,12]

def sum_of_pos(arr):
    res = 0
    for num in some_arr:
        if num > 0:
            res+=num
    return res

res = sum_of_pos([1,-4,7,12])
print(res)