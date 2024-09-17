import pyautogui as pag
import random
import sys
from time import sleep
filePath = "input.txt"
words = []
# check for passed args
if (len(sys.argv)>1):
    try:
        times = int(sys.argv[1]) # parse first arg as integer
    except ValueError:
        print("Error: input is not an int number") # if argument not integer, stop the script
        sys.exit()
elif (len(sys.argv)>2): # more then 1 argument
    print("You must pass only 1 argument")
    sys.exit()
else:
    times = 1 # default case on no args passed
# open file, read it line for line and store lines in list words
with open(filePath, "r") as file:
    for count, line in enumerate(file):
        words.insert(count, line.strip())

    print(f"{len(words)} total words from input")

for i in range(0, times):
    rand = random.randint(0, (len(words)-1)) # select a random word from list
    sleep(random.uniform(3,5))
    print(f"word: {words[rand]}, num = {rand+1} ({i+1}/{times})") # prints selected word, line of the word in input.txt and counter of cycles
    pag.typewrite(words[rand]) # write the word
    pag.press('enter') # send it
    sleep(random.uniform(1,3)) # wait for page to reload (NOTE: if you have a slow internet connection changing these numbers will give you more time to load the page)
    pag.click() # click on place (NOTE: you must place the cursor on the text field)
    pag.hotkey('ctrl','a') # select all to prepare for next cycle
