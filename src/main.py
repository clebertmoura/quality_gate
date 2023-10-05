acoes = input()
listacoes = acoes.split(' ')

listacount = []
listainicio = []

n=0
count = 0
inicio = 0
dizzy = False
while n < len(listacoes)-1:
    if listacoes[n] == 'staring' and listacoes[n+1] == 'away':
        if count == 0:
            inicio = n
            count += 1
        else:
            count += 1
        if n == len(listacoes)-2:
            listacount.append(count)
            listainicio.append(inicio)
        n+=2
        dizzy = True
    else:
        if count != 0:
            listacount.append(count)
            listainicio.append(inicio)
            count=0
        n+=1

if dizzy:
    maiorseq = max(listacount)
    maiorseqi = listainicio[listacount.index(max(listacount))]

    soma = 0
    x = 0
    while x < maiorseq*2:
        soma = soma + maiorseqi + x
        x += 1

    if soma%2 == 0:
        print('Só mais um surto do Yusuke...')
    else:
        print('Salve-se quem puder!')
else:
    print('Só mais um surto do Yusuke...')