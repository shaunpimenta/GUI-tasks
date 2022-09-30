dict1 = {"car": "cayane", "bike": "ninja", "location": "mumbai"}
dict2 = { "child": 2, "sport": "football", "location": "los angeles"}
list1 = dict1.keys()
list2 = dict2.keys()
for e in list2:
    dict1[e] = dict2[e]
print("Merged dictionary:- \n"+str(dict1))