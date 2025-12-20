# It plays a game once, generates a random score, compares it with the previous highest score stored in a file, and updates the file if the new score is higher.

import random

def game():
    print("you are playing the gane: ")
    score=random.randint(1,100)
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
        if (hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print('your score: ',score)
    if (score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
            
    return score

game()
