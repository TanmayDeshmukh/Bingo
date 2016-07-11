import sys
import random
tot=1
matrix_x=7
matrix_y=5
matrix_x=int(input('No. of columns: '))
matrix_y=int(input('No. of rows: '))

Arr=[[0 for x in range(matrix_x)]for y in range(matrix_y)]
for i in range(0,matrix_y):
    print(Arr[i])
def check():
    full=True
    for i in range(matrix_x):
        full=True
        for j in range(matrix_y):
            if(Arr[j][i]==0):
                full=False
                #break
        if(full):
            print "\n Bingo!\n Column: ",i+1
            return True
      
    for i in range(0,matrix_y):
        full=True
        for j in range(0,matrix_x):
            if(Arr[i][j]==0):
                full=False
                #break
        if(full):
            print "\n Bingo!\n Row: ",i+1
            return True
    return False

while(not check()):
    raw_input('\nRoll the dice?')
    number_on_dice=random.randint(1,6)
    
    sys.stdout.write('Number on the dice=')
    print(number_on_dice)
    
    if tot+number_on_dice<=matrix_x*matrix_y:
        tot+=number_on_dice
    else:
        tot=tot+number_on_dice-matrix_x*matrix_y
    #x=(tot-1)%matrix_x
    x=(tot-1)%matrix_x
    y=(tot-1)/matrix_x
    
    if(y%2==1):
        print "rev"
        print x
        x=matrix_x-1-x
    
    
    #if(matrix_x*matrix_y-tot<6 and matrix_x*matrix_y-tot>0):
    #    print 'You need ',matrix_x*matrix_y-tot,' or less to win'
    print "Dice on: ",tot
    print "X: ",x+1
    print "Y: ",y+1
    print "x:", x,"\ty:",y
    Arr[y][x]=1
    for i in range(0,matrix_y):
        print(Arr[i])
    
    
if(tot>matrix_x*matrix_y):
    print('Better luck next time')
else:
    print('You\'ve won!')
    
    

