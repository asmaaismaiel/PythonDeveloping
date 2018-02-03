print("Islam Mesha Python Developer")
word = input("Enter the word.\n")


def removeVowels(word):
    pass
    new_word = ""
    for letter in word:
        pass
    # print(letter)
        vowels = ('a', 'e', 'i', 'o', 'u')
        if letter not in vowels:
            pass
            new_word += letter
            # print(new_word)
        else:
            pass
            # print("Letter is a vowel !")
    return new_word
x = removeVowels(word)
print(x)