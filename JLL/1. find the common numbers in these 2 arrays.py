a = [ 2, 3, 4, 5, 7, 8, 10, 12 ] 
b = [ 1, 2, 3, 6, 12 ]

# 8, 5
i = 0
j = 0
res = []
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        res.append(a[i])
        i += 1
        j += 1
    elif a[i] > b[j]:
        j += 1
    else:
        i += 1
print(res)
    
