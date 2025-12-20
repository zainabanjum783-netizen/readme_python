# def mergeall(lis1,lis2,lis3,reverse=False):
#     lis=[]
#     lis.extend(lis1)
#     lis.extend(lis2)
#     lis.extend(lis3)
    
#     if reverse==True:
#         lis.reverse()
#     print(lis)

# mergeall([1,2,3],[4,5],[6,7,[8,9]])   
# mergeall([1,2,3],[4,5],[6,7,[8,9]]) 

def merge(*lists,reverse=False):
    result=[]
    
    for item in lists:
        for it in item:
            if isinstance(it,(list,tuple)):
                result.append(it)
            else:
                result.append(it)

    if reverse==True:
        result.reverse()
        
    print(result)
    
merge([1,2,3],[4,5],[6,7,[8,9]],reverse=True)
# merge([1,2,3],[4,5],[6,7,[8,[9,10]]])  
