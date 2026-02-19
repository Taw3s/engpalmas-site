saldo = 0
pendentes = [] 
while True:
    notas = float(input('Digite o valor da nota:'))
    if notas == '0':
        print('Encerrando o programa...')
        break
    
    elif notas > 10.000:
        pendentes.append(notas)
        print('Nota enviada para aprovação.')
    
    else:
        saldo = saldo + notas
        
        if saldo < 0:
                print('ALERTA DE AUDITORIA: Saldo negativo! Travando o programa.')
                break
print('O saldo total é:', saldo)
print('As notas pendentes são:', pendentes)
