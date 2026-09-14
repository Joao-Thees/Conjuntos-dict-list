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

def preco_de(estoque: dict, produto: str) -> float:

    if produto in estoque:
        return estoque[produto]['preco'] # 
    return 0.0
    
print(preco_de(ESTOQUE, 'X-Burguer'))

def vender(estoque: dict, vendas, produto, qtd) -> float:

    # simular venda
    # baixa automatica estoque

    if produto in estoque:
        return estoque
    return 0.0

print(vender('X-Burguer'))