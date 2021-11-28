produtos = []
produton = 0
valorn = 1

while True:
    produto = str(input('Nome do produto: '))
    produtos.append(produto)
    
    valor = float(input('Valor do produto: '))
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
    print(f'Produto: {produtos[produton]}....... Valor: R${produtos[valorn]}')
    produton += 2
    valorn += 2