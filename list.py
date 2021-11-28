produtos = []

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
for p in produtos:
    print(p)