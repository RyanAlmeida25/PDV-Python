import os
import datetime
import dados
from dados import clientes
from dados import produtos
from dados import vendedores
from dados import lista_produtos
from dados import comissao_vendedores
from dados import vendas 
from dados import imposto
from dados import produtos_vendidos

def dados_cliente(codigo, nome):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            print(f"Código {codigo} já está cadastrado para o cliente {cliente['nome']}.")
            return
    cliente = {
        'codigo': codigo,
        'nome': nome
    }
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso.")


def cadastro():
    print("Deseja cadastrar um novo cliente? (s/n)")

    if input().lower() != 's':
        print("Saindo do sistema de cadastro.")
        return 
    while True: 
        try: 
            codigo = int(input("Codigo do cliente: "))
        except ValueError: 
            print("Código inválido.")
            continue 
        nome = input("Nome do cliente: ")
        dados_cliente(codigo, nome) 
        salvar_dados() 
        continuar = input("Deseja cadastrar outro cliente? (s/n): ")
        if continuar.lower() != 's':
            break
        print("Saindo do sistema de cadastro.")



def dados_produto(codigo, nome, valor, estoque):
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"Código {codigo} já está cadastrado para o produto {produto['nome']}.")
            return
    produto = {
        'codigo': codigo,
        'nome': nome,
        'valor': valor,
        'estoque': estoque
    }
    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso.")


def cadastro_produto():
    print("Deseja cadastrar um novo produto? (s/n)")
    if input().lower() != 's':
        print("Saindo do sistema de cadastro.")
        return
    while True:
        try:
            codigo = int(input("Código do produto: \n"))
            nome = input("Nome do produto: \n")
            valor = float(input("Valor do produto: \n"))
            estoque = int(input("Quantidade em estoque: \n"))
        except ValueError:
            print("Dados inválidos. Tente novamente.")
            continue
        dados_produto(codigo, nome, valor, estoque)
        salvar_dados()
        continuar = input("Deseja cadastrar outro produto? (s/n): ")
        if continuar.lower() != 's':
            break
    print("Saindo do sistema de cadastro de produtos.")
    

def dados_vendedores(codigo, nome, comissao=0):
    for vendedor in vendedores:
        if vendedor['codigo'] == codigo:
            print(f"Código {codigo} já está cadastrado para o vendedor {vendedor['nome']}.")
            return
    vendedor = {
        'codigo': codigo,
        'nome': nome,
    }
    vendedores.append(vendedor)
    print(f"Vendedor {nome} cadastrado com sucesso.")


def cadastro_vendedor():
    print("Deseja cadastrar um novo vendedor? (s/n)")
    if input().lower() != 's':
        print("Saindo do sistema de cadastro.")
        return
    while True:
        try:
            codigo = int(input("Código do vendedor: \n"))
            nome = input("Nome do vendedor: \n")
        except ValueError:
            print("Dados inválidos. Tente novamente.")
            continue
        dados_vendedores(codigo, nome)
        salvar_dados()
        continuar = input("Deseja cadastrar outro vendedor? (s/n): ")
        if continuar.lower() != 's':
            break
    print("Saindo do sistema de cadastro de vendedores.")


def salvar_dados():
    caminho = os.path.join(os.path.dirname(__file__), 'dados.py') 
    try:
        with open(caminho, 'w') as f: 
            f.write(f"clientes = {repr(clientes)}\n") 
            f.write(f"produtos = {repr(produtos)}\n")
            f.write(f"vendedores = {repr(vendedores)}\n") 
            f.write(f"comissao_vendedores = {repr(comissao_vendedores)}\n") 
            f.write(f"lista_produtos = {repr(lista_produtos)}\n")
            f.write(f"vendas = {repr(vendas)}\n")
            f.write(f"imposto = {repr(imposto)}\n")
            f.write(f"produtos_vendidos = {repr(produtos_vendidos)}\n")
        print("Dados salvos com sucesso em dados.py.")
    except Exception as e: 
        print(f"Erro ao salvar os dados: {e}")

def verificar_cliente():
    try:
        codigo_cliente = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return verificar_cliente()

    cliente_cadastrado = None
    for cliente in clientes:
        if cliente['codigo'] == codigo_cliente:
            cliente_cadastrado = cliente
            break

    if cliente_cadastrado:
        print(f"Cliente cadastrado: {cliente_cadastrado['nome']}")
        return verificar_vendedor() 

    else:
        print("Cliente não cadastrado.")
        print("Deseja cadastrar o cliente? (s/n)")
        if input().lower() == 's':
            cadastro()
            return verificar_cliente()
        else: 
            print("Compra não permitida. Cliente não cadastrado.")
            return False
            

def verificar_vendedor():

    codigo_vendedor = int(input("Digite o código do vendedor: "))
    vendedor_cadastrado = None 

    for vendedor in vendedores: 
        if vendedor['codigo'] == codigo_vendedor: 
            vendedor_cadastrado = vendedor
            break

    if vendedor_cadastrado:
        print(f"Vendedor cadastrado: {vendedor_cadastrado['nome']}")
        return vendedor_cadastrado
    
    else:
        print("Vendedor não cadastrado.")
        print("Deseja cadastrar o vendedor? (s/n)")
        if input().lower() == 's':
            cadastro_vendedor()
            return verificar_vendedor()
        else:
            print("Compra não permitida. Vendedor não cadastrado.")
            return False



def verificar_produto(vendedor):
    codigo_produto = int(input("Digite o código do produto: "))
    produto_cadastrado = None 
    produto_estoque = None 
    

    for produto in produtos: 
        if produto['codigo'] == codigo_produto: 
            print(f"Produto cadastrado: {produto['nome']}")
            produto_cadastrado = produto 
            produto_estoque = produto
            break
    
    if produto_estoque:
        if produto_estoque['estoque'] <= 0: 
            print(f"{produto_estoque['nome']} fora de estoque.")
            print("Compra não permitida.")
            return False
        else:
            print(f"Produto em estoque")
            lista_produtos.append(produto_estoque)


            print("Deseja adicionar outro produto? (s/n)")
            if input().lower() != "s":
                salvar_dados()
                return True
            else:
                verificar_produto(vendedor)
                return True
            





    else:
        print("Produto não cadastrado.")
        print("Deseja cadastrar o produto? (s/n)")
        if input().lower() == 's':
            cadastro_produto()
            return verificar_produto()
        else:
            print("Compra não permitida. Produto não cadastrado.")
            return False


def verificacao_compra():
    if verificar_cliente() and verificar_vendedor: 
        print("Verificação permitida.")
    else:
        print("Verificação negada.")
        return False


def compra():
    print("Bem vindo ao sistema de compras.")
    print("Insira os dados do vendedor: ")
    vendedor = verificar_vendedor()
    valor_total = 0
    verificar_produto(vendedor)
    quantidade_estoque = {}

    for item in lista_produtos:
        print(f"Produto adicionados: {item['nome']}, Valor: R${item['valor']}. Vendedor: {vendedor['nome']}")
    print("Deseja finalizar a compra? (s/n)")
    if input().lower() == 's':
        for valor in lista_produtos:
            valor_total += valor['valor']
    
        for item in lista_produtos:
            cod = item['codigo']
            quantidade_estoque[cod] = quantidade_estoque.get(cod, 0) + 1

        for produto in produtos:
            codigo = produto['codigo']
            if codigo in quantidade_estoque:    
                produto['estoque'] -= quantidade_estoque[codigo]
            
        comissao_vendedor = valor_total * 0.05
        
        comissao_vendedores.append({
            'vendedor': vendedor['nome'],
            'comissao': f"{comissao_vendedor:.2f}"
            })
        
        total_vendas = {
            'valor total': valor_total,
            'data': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }



        print(f"Itens comprados: {len(lista_produtos)}")
        print(f"Compra: {','.join([item['nome'] for item in lista_produtos])}")
        print(f"Valor total da compra: R${valor_total:.2f}")
        print(f"Compra realizada por: {vendedor['nome']}")
        print(f"Data da compra: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

        for produto_vendido in lista_produtos:
            produtos_vendidos.append(produto_vendido['nome'])
        lista_produtos.clear()
        vendas.append(total_vendas)
        salvar_dados()

    else:
        print("Compra cancelada.")
        return False
    

def calcular_imposto():
    soma_valor = 0
    for venda in vendas:
        soma_valor += venda['valor total']
    
    imposto_dia = soma_valor * 0.25
    print(f"Imposto (25%) sobre R${soma_valor:.2f}: R${imposto_dia:.2f}")
    dados_imposto = {
        'imposto': imposto_dia,
        'data': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }
    imposto.append(dados_imposto)
    salvar_dados()


def relatorio():
    print(f"Relatório, Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: \n")
    for v in vendas:
        print(f"Data: {v['data']}, Valor total: R${v['valor total']:.2f}\n")

    for p in produtos:
        print(f"Produto: {p['nome']}, Código: {p['codigo']}, Valor: R${p['valor']:.2f}, Estoque: {p['estoque']}\n")
    
    for valor in imposto:
        print(f"Data: {valor['data']}, Imposto: R${valor['imposto']:.2f}\n")
    
    print("Comissão por vendedor:\n")
    
    for c in comissao_vendedores:
        print(f"Vendedor: {c['vendedor']}, Comissão: R${c['comissao']}\n")
    
    produtos_vendidos.clear()
    salvar_dados()