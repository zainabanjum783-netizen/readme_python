def order_summary(order_id, *items, tax=0.05, **special_charges):
    le=len(items)
    lis=[]
    b=0
    while(b<le):
        lis.insert(b,items[b][1]*items[b][2])
        b+=1
    subtotal=sum(lis)
    xat=subtotal*tax
    total=subtotal+xat+sum(special_charges.values())
    
    print(f"""order summary\n
-----------------\n
order id: {order_id}\n 
-----------------\n
items
-----------------""")
    b=0
    while b<le:
        print(f"{items[b][0]}(0{items[b][1]})={lis[b]}\n")
        b+=1
    print(f"""sub total: {subtotal}\ntax: {xat}\ntotal bill: {total}""")

order_summary(102,*(('brush',5,50),('toothpaste',5,20)),delivery=30)  
    
    # (item_name, qty, price)
    # sub total 
    # tax
    # total amount