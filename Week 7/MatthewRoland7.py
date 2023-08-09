def power(base, pow):
    if pow == 1:
        return base
    elif pow == 0:
        return 1
    elif pow < 0:
        return 1 / power(base, -pow)
    
    return base * power(base, pow-1)

def cat_ears(cats):
    if cats <= 0:
        return 0
    
    return 2 + cat_ears(cats-1)

def alien_ears(aliens):
    if aliens == 1:
        return 3
    elif aliens %2 == 0:
        return 2 + alien_ears(aliens-1)
    elif aliens %2 == 1:
        return 3 + alien_ears(aliens-1)

    return 

if __name__ == "__main__":
    x,y = 5,-1
    print(power(x,y))
    print(alien_ears(x))
