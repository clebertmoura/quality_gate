def fibonacci(x):
    if x <= 1:
        return 1
    else:
        return(fibonacci(x - 1) + fibonacci(x - 2))        

valores = input().split()
vidas = int(valores[0])
casas = int(valores[1])
lista_fibonacci = [0]
contador_casas = 0

while vidas != 0:
        contador_casas += 1
        lista_fibonacci.append(fibonacci(contador_casas))
        num_casa = int(input())
        if num_casa in lista_fibonacci:
            if casas == contador_casas:
              if vidas != 0:
                print(""Voce Adicionou A Master Sword ao seu inventario"")
                print('Link Salve Hyrule!!!')
                vidas = 0
                    #Parar de rodar o código
        else:
            if vidas != 0:
                print('Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!')
                vidas -= 1
                contador_casas = 0
                lista_fibonacci = [] #resetando a lista com fibonacci
            if vidas == 0:
                print('A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf')