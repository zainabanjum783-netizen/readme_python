import matrixdisplay as md
import random as r

user=input('enter your choice: o or x: \n')
if user=='o':
    computer='x'
else:
    computer='o'
    
print('Enter 0 for your first turn and enter 1 for computer\'s first turn')
chance=int(input())

choice=[1,2,3,4,5,6,7,8,9]

while chance<10:
    if chance%2==0:
        if chance==0:
            md.display()
        uc=int(input(f'enter your choice for: {user}\n'))
        for row in md.matrix:
            for col in row:
                if col==uc:
                    md.matrix[md.matrix.index(row)][row.index(col)]=user
                    choice.remove(uc)
        chance+=1
    else:
        cc=r.choice(choice)
        for row in md.matrix:
            for col in row:
                if col==cc:
                    md.matrix[md.matrix.index(row)][row.index(col)]=computer
                    print('THE BOARD')
                    md.display()
                    choice.remove(cc)
        chance+=1
    if (md.check()==1):
        if computer=='o':
            print('computer won! you lost')
            break
        else:
            print('you won!')
            break
    elif (md.check()==0):
        if computer=='x':
            print('computer won! you lost')
            break
        else:
            print('you won')
            break

    if chance==9:
        print('It\'s a draw')
        break