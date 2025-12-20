#merge list and flatten it one level

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
