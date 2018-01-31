def calc(num):
    pass
    myList = []
    for i in range(0, num):
        pass
        myList2 = []
        for j in range(i + 1):
            pass
            myList2.append((j + 1) * (i + 1))
        myList.append(myList2)
    return myList


num = int(input("Enter the Number "))
myList = calc(num)
print(myList)