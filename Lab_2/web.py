import webbrowser
# import math
import random
# Write a program that choose a random website name from list and open it in your browser :


def makeUrl():
    pass
    url = ['http://docs.python.org/', 'http://fb.com/', 'http://google.com/',
           'https://git.com/', 'https://www.youtube.com/']
    link = url[random.randint(0, 4)]
    return link


link = makeUrl()
# webbrowser.open_new(link)
print(link)
