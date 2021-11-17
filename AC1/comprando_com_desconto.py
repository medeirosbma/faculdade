preco_mercadoria = float(input())
quantidade_itens = int(input())

venda_s_desc = preco_mercadoria * quantidade_itens

desc_fixo = venda_s_desc * 0.10
desc_quantidade = quantidade_itens * 0.01
desc_por_mercadoria = venda_s_desc * desc_quantidade

venda_c_desc = venda_s_desc - desc_fixo - desc_por_mercadoria

print(f'{venda_s_desc:.2f}')
print(f'{venda_c_desc:.2f}')