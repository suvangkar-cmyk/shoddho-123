test_dict = {'codingal': 3 , 'is':3, 'best':3,'for':3, 'coding':3}
print("The original dictionary :"  + str(test_dict))
k = 3
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
print("frequency of k is: "  + str(res))
