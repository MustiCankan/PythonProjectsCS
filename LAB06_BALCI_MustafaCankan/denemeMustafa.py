def isDelectable(number):
    a = str(number)
    for i in range(1,len(a) + 1):
        c = int(a[:i])
        if c % i != 0:
               return False
    return True

def seperateDelectable(l):
    k = l[::]
    s = []
    for j in k:
        if isDelectable(j):
            l.remove(j)
            s.append(j)
    return s



l = [4236,2052,1425]
print(seperateDelectable(l))
print(l)
