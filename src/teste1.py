def procurador(x,y):
    if len(x) == 0 or len(y) == 0:
        return 0
    else:
        posicao = y.find(x)
        return y[posicao:posicao + len(x)]
      
suspeito = str(input())
analisados = str(input()).lower()

suspeito_minusc = suspeito.lower()

if procurador(suspeito_minusc, analisados) == suspeito.lower():
  print(f'Encontrei, o culpado é o {suspeito}!')
else:
  print(f'Não era o {suspeito}, tenho que continuar procurando.')