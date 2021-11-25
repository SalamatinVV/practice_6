def chop(t) :
    for i in range(2):
        t.pop(0)
        t.reverse()

t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(chop(t))