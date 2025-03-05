a = [1,2,3,4,5]


result = []
for i in range(len(a)):
    rotate = a[i:]+a[:i]
    result.append(rotate)

print(result)

    

