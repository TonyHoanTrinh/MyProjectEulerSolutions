for a in range(1,499):
    for b in range(a + 1,500):
        c = 1000 - b - a
        if(a ** 2 + b ** 2 == c ** 2):
            print(a * b * c)
            break
