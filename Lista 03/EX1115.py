control = True

while control:
    x, y = map(int,input('').strip().split())
    
    if x == 0 or y == 0:
        control = False
    else:
        if x > 0 and y > 0:
            print('primeiro')
        elif x > 0 and y < 0:
            print('quarto')
        elif x < 0 and y > 0:
            print('segundo')
        else:
            print('terceiro')