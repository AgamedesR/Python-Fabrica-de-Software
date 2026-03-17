import requests

resposta = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")

print('Status da Requesição: ', resposta.status_code)
print('Respota da API: ', resposta.json())

# USAR PANDAS AQUI