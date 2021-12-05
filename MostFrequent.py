W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
 
sn = most_frequent(W)
L1 =[(k,v) for k, v in sn.items()]
L1.sort(key=lambda i:i[1],reverse=True)
print(L1)
