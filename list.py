produtos = []
produton = 0
valorn = 1
valor_geral = 0

print('____________________________________')
print()
print('*         Lista de compras         *')
print('____________________________________')
print()

while True:
    produto = str(input('Nome do produto: '))
    produtos.append(produto)
    
    valor = int(input('Valor do produto: '))
    produtos.append(valor)
    valor_geral += valor
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

print()
print('Lista de compras:')
print()

while total() > valorn:
    print(f'Produto: {produtos[produton]}....... Valor: R${produtos[valorn]}')
    produton += 2
    valorn += 2
    print('---')


gerar = str(input('\nVocê quer gerar um arquivo?'))
try:
    if gerar == 'y':
        arquivo = open('lista.txt', 'w')
        produton = 0
        valorn = 1
        for p in produtos:
            arquivo.write(f'Produto:{produtos[produton]}\nValor: {produtos[valorn]}')
            arquivo.write(' \n')
            valorn += 2
            produton += 2
    else:
        exit()
except:
    print()