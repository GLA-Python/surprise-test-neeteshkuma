def expanding(lst):
    lst2=[]
    for i in range(1,len(lst)):
        d=lst[i]-lst[i-1]
        lst2.append(abs(d))
    e=True
    for i in range(1,len(lst2)):
        if lst2[i]<=lst2[i-1]:
            e=False
            break
    
    return e


lst=list(map(int,input().split()))
print(expanding(lst))
