def compute():
    sum = 0
    for x in range(1000):
        if(x % 3 == 0 or x % 5 == 0):
            sum += x
    
    return str(sum)


if __name__ == "__main__":
    print(compute())
