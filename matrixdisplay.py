matrix=[[1,2,3],[4,5,6],[7,8,9]]
def display(): 
    for row in matrix:
        print(f'--------------------------\n|       |       |       |')
        for col in row:
            print('| ',col,'   ',end='')
        print('|\n|       |       |       |')
    
def check():
    for row in matrix:
            if len(set(row))==1 and row[0]=='o':
                return 1
            elif len(set(row))==1 and row[0]=='x':
                return 0
                
    b=0

    while b<3:
        c=0
        lis=[]
        while c<3:
            lis.append(matrix[c][b])
            c+=1
        if len(set(lis))==1 and lis[0]=='o':
            return 1
        elif len(set(lis))==1 and lis[0]=='x':
            return 0
            
        b+=1
        
    lisd=[matrix[0][0],matrix[1][1],matrix[2][2]]
    if len(set(lisd))==1 and lisd[0]=='o':
        return 1
    elif len(set(lisd))==1 and lisd[0]=='x':
        return 0
        
    lis2d=[matrix[0][2],matrix[1][1],matrix[2][0]]
    if len(set(lis2d))==1 and lis2d[0]=='o':
        return 1
    elif len(set(lis2d))==1 and lis2d[0]=='x':
        return 0
        