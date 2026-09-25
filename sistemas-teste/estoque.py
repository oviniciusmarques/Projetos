products  = [] # lista
next_id = 1 # contador
total_prod = 0
total_stock = 0
value_stock_total = 0

def get_number(pergunta, mensagem_erro, valor_minimo, mensagem_minimo, tipo, valor_maximo=None):
    while True:
        try:
            numero = tipo(input(pergunta))
            if numero < valor_minimo:
                 print(mensagem_minimo)
                 continue
            if valor_maximo != None:
                if numero > valor_maximo:
                    print(mensagem_minimo)
                    continue
            return numero
        except ValueError:
            print(mensagem_erro)
            continue


def cadastrar_produto():
    global next_id, total_prod, total_stock, value_stock_total
    while True:
        name = str(input('Digite o nome do produto: ')).strip().capitalize()
        if name == "":
            print('Erro. O nome não pode estar vazio!')
            continue
        break
    description = str(input('Digite a descrição do produto: ')).strip()
    price = get_number('Digite o preço do produto: ',
                    'Erro. Digite uma opção válida!',
                    1,
                    'Erro. O preço deve ser maior que 0!',
                    float)
    quantity = get_number('Digite a quantidade de unidades do produto: ',
                        'Erro. Digite um número válido!',
                        1, 
                        'Erro. A quantidade deve ser maior que 0!',
                        int)
    while True:
        category = str(input('Digite a categoria do produto: ')).strip().capitalize()
        if category == "":
            print('Erro. A categoria não pode estar vazia!')
            continue
        break
    value_stock_prod = price * quantity

    product = {
        'id' : next_id,
        'name' : name,
        'description' : description,
        'price' : price,
        'quantity' : quantity,
        'category' : category,
        'value_stock_prod' : value_stock_prod
    }

    products.append(product)

    next_id += 1
    total_prod += 1
    total_stock += quantity
    value_stock_total += value_stock_prod

    print('PRODUTO ADICIONADO COM SUCESSO!')

def listar_produtos():
    print(products)

def buscar_produto():
    produto_encontrado = False
    busca = str(input('Digite o nome do produto que deseja buscar: ')).strip().capitalize()
    for product in products:
        if busca == product['name']:
            print(product)
            produto_encontrado = True
    if not produto_encontrado:
        print('Produto não econtrado!')

def remover_produto():
    global total_prod, total_stock, value_stock_total
    produto_encontrado = False
    remove = get_number('Qual é o ID do produto que deseja remover?: ',
                           'Erro. Digite um ID válido!',
                           1,
                           'Erro. A quantidade a ser removida deve ser maior que 0!',
                           int)
    for product in products:
        if remove == product['id']:
            total_prod -= 1
            total_stock -= product['quantity']
            value_stock_total -= product['value_stock_prod']
            products.remove(product)
            print(f'O produto {remove} foi removido!')
            produto_encontrado = True
            break
    if not produto_encontrado:
        print('Produto não encontrado!')

def entrada_estoque():
    global total_stock, value_stock_total
    produto_encontrado = False
    atualizado = get_number('Qual é o ID do produto que deseja atualizar?: ',
                             'Erro. Digite um ID válido!',
                             1,
                             'Erro. A quantidade a ser atualiza deve ser maior que 0!',
                             int)
    entrada = get_number('Qual é a quantidade que está adicionando?: ',
                          'Erro. Digite um número válido!',
                          1,
                          'Erro. A quantidade de entrada deve ser maior que 0!',
                          int)
    if entrada <= 0:
        print('ERRO. Digite um número maior que zero!')

    else:
        for product in products:
            if atualizado == product['id']:
                total_stock += entrada
                product['quantity'] += entrada
                product['value_stock_prod'] += entrada * product['price']
                value_stock_total += entrada * product['price']
                print(f'Foram adicionados mais {entrada} unidades do id {atualizado}, totalizando agora {product["quantity"]} unidades')
                produto_encontrado = True
                break
        if not produto_encontrado:
            print('Produto não encontrado!')

def saida_estoque():
    global total_stock, value_stock_total
    produto_encontrado = False
    atualizado = get_number('Qual é o ID do produto que deseja atualizar?: ',
                             'Erro. Digite um ID válido!',
                             1,
                             'Erro. Nenhum id é menor do que 0!',
                             int)
    saida = get_number('Qual é a quantidade que esta retirando?: ',
                        'Erro. Digite um número válido',
                        1,
                        'Erro. A quantidade deve ser maior que 0!',
                        int)

    if saida <= 0:
        print('ERRO. Digite um número maior que zero!')

    else:
        for product in products:
            if atualizado == product['id']:
                if saida > product['quantity']:
                    print(f'Baixa negada, temos {product["quantity"]} unidades em estoque!')
                    produto_encontrado = True
                    break

                else:
                    total_stock -= saida
                    product['quantity'] -= saida
                    value_stock_total -= saida * product['price']
                    product['value_stock_prod'] -= saida * product['price']
                    print(f'Foram retirados {saida} unidades do id {atualizado}, totalizando agora {product["quantity"]} unidades')
                    produto_encontrado = True
                    break

        if not produto_encontrado:
            print('Produto não encontrado!')

def estatistica_estoque():   
    if not products:
        print('Não há produtos cadastrados para exibir estatísticas')
        return

    maior = products[0]['quantity']
    produto_maior = products[0]['name']
    menor = products[0]['quantity']
    produto_menor = products[0]['name']

    for product in products:
        if product['quantity'] > maior:
            maior = product['quantity']
            produto_maior = product['name']

        if product['quantity'] < menor:
            menor = product['quantity']
            produto_menor = product['name']

    print(f'Temos {total_prod} produtos no estoque!')
    print(f'Temos {total_stock} unidades em estoque!')
    print(f'O estoque tem um valor total de {value_stock_total:.2f}R$ em produtos!')
    print(f'O produto com mais estoque é {produto_maior} com {maior} unidades')
    print(f'O produto com menor estoque é {produto_menor} com {menor} unidades')
            
print('Bem vindo ao nosso sistema de estoque!')

while True:

    print('===== MENU ESTOQUE =====')
    print('[ 1 ] Cadastrar produto\n[ 2 ] Listar produtos\n[ 3 ] Buscar produtos\n[ 4 ] Remover produto\n[ 5 ] Entrada e baixa\n[ 6 ] Estatísticas\n[ 7 ] Encerrar programa')
    escolha = get_number('escolha uma opção: ',
                          'Erro. Digite uma opção válida!',
                          1,
                          'Erro. Digite algum número de 1 a 7!',
                          7,
                          int)

    if escolha == 1:
        cadastrar_produto()
        
    elif escolha == 2:
        listar_produtos()

    elif escolha == 3:
        buscar_produto()

    elif escolha == 4:
        remover_produto()

    elif escolha == 5:
        print('[ 1 ] Entrada\n[ 2 ] Saída')
        opcao = get_number(
            'Digite o numero da opção que deseja: ', 
            'Opção inválida',
            1,
            'Erro. Digite um numero de 1 a 2!',
            2,
            int
            )
        
        if opcao == 1:
            entrada_estoque()
        
        if opcao == 2:
            saida_estoque()
            
    elif escolha == 6:
        estatistica_estoque()

    elif escolha == 7:
        print('Encerrando o programa...')
        break