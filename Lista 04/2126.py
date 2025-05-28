try:
    caso = 1 
    while True:
        cont = 0
        lista_n2 = []
        while cont < 2:
            n1 = int(input())
            n2 = input()
            n2_list = list(map(int, n2.split()))
            lista_n2.extend(n2_list)
            cont += 1
        
        sub = len(lista_n2)
        
        print(f'Caso #{caso}')
        print(f'Qtd.subsequencias: {sub}')
        caso += 1

except EOFError:
    pass