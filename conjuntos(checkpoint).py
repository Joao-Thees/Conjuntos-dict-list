# conjuntos

# sem indice e ordem, principal vantagem é que é mais rapido e limpa dados
# set()
# muito usado para limpar dados sujos
# relembrando: sorted da na ordem crescente
# exemplo:
# metodo .add adicixona individualmente
# metodo update adixciona mais de um metodo
# metodo discard rexmove 
# remove remove masx nao permite itens inexistentes

'''def conjuntos():

    sku = {'ABCDEFG12345'}
    sku.add('ABCDEFGHIJ12345678')
    sku.update(['abc', 'def'])
    sku.discard('def')
    return sku

print(conjuntos())'''

ESTOQUE = {
    "X-Burguer": {"preco": 18.50, "qtd": 10},
    "X-Salada": {"preco": 20.00, "qtd": 6},
    "Batata frita": {"preco": 10.00, "qtd": 8},
    "Açaí 300ml": {"preco": 12.00, "qtd": 5},
    "Suco de laranja": {"preco": 8.00, "qtd": 10},
    "Refrigerante lata": {"preco": 6.50, "qtd": 24},
    "Água mineral": {"preco": 4.00, "qtd": 0},
}

INGREDIENTES = {
    "X-Burguer": {"pao", "carne", "queijo"},
    "X-Salada": {"pao", "carne", "queijo", "alface", "tomate"},
    "Batata frita": {"batata", "sal"},
    "Açaí 300ml": {"acai", "granola"},
    "Suco de laranja": {"laranja"},
}

vendas = []


def preco_de(estoque: dict, produto: str) -> float:

    if produto in estoque:
        return estoque[produto]['preco'] # 
    return 0.0
    
print(preco_de(ESTOQUE, 'X-Burguer'))

def tem_estoque(estoque:dict, produto:str, qtd:int) -> bool:
    if produto in estoque:
        return estoque[produto]['qtd'] >= qtd # [chave]['valor']
    return False

print(tem_estoque(ESTOQUE, "X-Burguer", 20)) # 3 parametro é a qtd pedida
print(tem_estoque(ESTOQUE, 'Água mineral', 1))

def vender(estoque: dict, vendas:list, produto:str, qtd:int) -> float:
    if not tem_estoque(estoque, produto, qtd): # se nao tem
        return 0.0

    else: # SE TEM
        valor = qtd * preco_de(estoque, produto)
        # como descontar qtd do estoque
        estoque[produto]['qtd'] -= qtd
        vendas.append([produto, qtd, valor])

        return valor
vendas = []
print(vender(ESTOQUE, vendas, "X-Burguer", 2))