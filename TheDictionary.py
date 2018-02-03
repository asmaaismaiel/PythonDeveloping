# myDictionary = {}
# myList = ["ahmed", "fatma", "Ibrahim"]
# myList.sort()
# print(myList)
# for i in range(len(myList)):
#     pass
#     myDictionary[myList[i][0]] = myList[i]
# print(myDictionary)
# List2 = [x[0] for x in myList]
# d = zip(List2, myList)
# print(dict(d))
def convert(names):
    pass
    names.sort()
    result = {}
    for name in names:
        if name[0] in result:
            pass
            result[name[0]].append(name)
        else:
            pass
            result[name[0]] = [name]
    return result


res = convert(["ahmed", "fatma", "Ibrahim", "Islam", "Samah"])
print(res)