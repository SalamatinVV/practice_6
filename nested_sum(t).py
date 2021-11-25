t = [[5,4,6],[8,4,2],[9,4,2]]
def nested_sum(t) :
    c=0
    for i in t :
        c +=sum(i)
    print (c)
nested_sum(t)