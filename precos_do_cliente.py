precos_do_cliente = [150.00, 400.00, 300.00, -10.00, 500.00]
total_a_pagar = 0
for preco in precos_do_cliente:
    if preco < 0:
        print('Falha no leitor! Parando a leitura...')
        break
    elif preco >= 300:
        print('Desconto aplicado para o item de preço 300.00')
        total_a_pagar += (preco - 50)
    else:
        print(f'Item adicionado: R$ {preco:.2f}')
        total_a_pagar += preco
    
print('Total a pagar:', total_a_pagar)