# a monotonic increasing array is
# when, for an element in the array the next one is greater or equal

# a monotonic decreasing array is
# when, for an element in the array the next one is lesser or equal

size=int(input('enter the size of the array: '))
lis=[]
b=0
while b<size:
    lis.append(int(input('enter an integer element: ')))
    b+=1

print(lis)

flagd=True
flagi=True
a=1
while a<size:
    if  (lis[a-1]>lis[a]):
        flagi=False
        a+=1
    elif (lis[a-1]<lis[a]):
        flagd=False
        a+=1
    a+=1
        
if flagd==True:
    print('the array is decreasingly monotonic')
elif flagi==True:
    print('the array is increasingly monotonic')
else:
    print('the array is neither increasingly nor decreasingly monotonic')
