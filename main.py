import pyautogui as pag
import random
import sys
from time import sleep
filePath = "input.txt"
words = []
if (len(sys.argv)>1):
    try:
        times = int(sys.argv[1])
    except ValueError:
        print("Error: input is not an int number")
        sys.exit()
elif (len(sys.argv)>2):
    print("You must pass only 1 argument")
    sys.exit()
else:
    times = 1
    
with open(filePath, "r") as file:
    for count, line in enumerate(file):
        words.insert(count, line)

    print(f"{len(words)} total words from input")

for i in range(0, times):
    rand = random.randint(0, (len(words)-1))
    sleep(random.uniform(3,5))
    print(f"word: {words[rand]}, num = {rand}")
    pag.typewrite(words[rand])
    pag.press('enter')
    sleep(random.uniform(1,3))
    pag.click()
    pag.hotkey('ctrl','a')
