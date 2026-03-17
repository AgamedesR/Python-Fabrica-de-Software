# Constante (IVA = Imposto sobre Valor Acrescentado)
IVA = 0.23  # 23% de imposto

# Preços dos produtos
preco_camisa = 50.00
preco_sapato = 120.00
preco_calca = 80.00

# Calculando o imposto de cada produto
imposto_camisa = preco_camisa * IVA
imposto_sapato = preco_sapato * IVA
imposto_calca  = preco_calca  * IVA

# Preço final
print(f"Camisa: R$ {preco_camisa + imposto_camisa:.2f}")
print(f"Sapato: R$ {preco_sapato + imposto_sapato:.2f}")
print(f"Calça:  R$ {preco_calca  + imposto_calca:.2f}")