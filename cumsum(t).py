t = [[5,4,6],[8,4,2],[9,4,2]]
cum_t = [[],[],[]]
def cumsum(t) :
    c=0
    l=0
    s=0
    for i in t :
        for k in i :
            c+=k
            cum_t[s].append(c)
            l+=1
            if l==3 :
                s+=1
    print (cum_t)
cumsum(t)