def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]
                                                  
                                    
n = route_num(20)
                    
print (n)

c = 1
for i in range(1,21):
    c = c * (20 + i)/ i
print(c)

