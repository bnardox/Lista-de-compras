produtos = []
produton = 0
valorn = 1


print('____________________________________')
print()
print('*         Lista de compras         *')
print('____________________________________')
print()

while True:
    produto = str(input('Nome do produto: '))
    produtos.append(produto)
    
    valor = input('Valor do produto: ')
    produtos.append(valor)

    confirm = str(input('Quer adicionar outro produto?[Y/N] ')).lower()
    if confirm == 'y':
        continue
    else:
        break

def total():
    contador = 0
    for p in produtos:
        contador += 1
    return contador

while total() > valorn:
    print(f'\nProduto: {produtos[produton]}....... Valor: R${produtos[valorn]}')
    produton += 2
    valorn += 2


gerar = str(input('\nVocê quer gerar um arquivo?'))
if gerar == 'y':
    arquivo = open('lista.txt', 'w')
    produton = 0
    valorn = 1
    for p in produtos:
        arquivo.write(f'Produto:{produtos[produton]} Valor: {produtos[valorn]}')
        arquivo.write(' \n')
        valorn += 2
        produton += 2