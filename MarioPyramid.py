sympol = input("Enter your sympol\n")
count = int(input("Enter the count of lines\n"))
for i in range(count):
    i += 1
    print(" " * (count - i), sympol * i)