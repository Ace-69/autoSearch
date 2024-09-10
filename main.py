import pyautogui as pag
import random
import sys
from time import sleep
filePath = "valid-wordle-words.txt"
words = []
if (sys.argv[1]):
    times = int(sys.argv[1])
else:
    times = 36
    
with open(filePath, "r") as file:
    for count, line in enumerate(file):
        words.insert(count, line)

    print(f"{len(words)} total words from wordle")

for i in range(0, times):
    rand = random.randint(0, (len(words)-1))
    sleep(random.uniform(3,5))
    print(f"word: {words[rand]}, num = {rand}")
    pag.typewrite(words[rand])
    pag.press('enter')
    sleep(random.uniform(1,3))
    pag.click()
    pag.hotkey('ctrl','a')
