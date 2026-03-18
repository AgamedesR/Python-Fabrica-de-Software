# KeyError:

# dados = {
#     "nome": "Isaac ",
#     "idade": 25,
#     "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")

# print(f"O valor da chave '{chave}' é: {dados[chave]}")

# Correção do Erro:

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}
 
chave = input("Digite a chave que deseja acessar: ")

valor = dados.get(chave, "Chave não encontrada!")
print(f"O valor da chave '{chave}' é: {valor}")