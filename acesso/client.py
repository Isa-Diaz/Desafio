import requests

url_acess = "http://127.0.0.1:5000/"
endpoint_base = "clientes"

def listar_clientes():
    url_nova = url_acess + endpoint_base
    result = requests.get(url_nova)
    dados = result.json()
    return dados

def buscar_cliente_por_id(id):
    id = str(id)
    url_nova = url_acess + endpoint_base + "/" + id
    result = requests.get(url_nova)
    dados = result.json()
    return dados

def criar_cliente(dados):
  url_nova = url_acess + endpoint_base
  result = requests.post(url_nova, json=dados)
  resposta = result.json()
  return resposta

def atualizar_cliente(id, dados):
   id = str(id)
   url_nova = url_acess + endpoint_base + "/" + id
   result = requests.put(url_nova, json=dados)
   resposta = result.json()
   return resposta
  
def deletar_cliente(id):
   id = str(id)
   url_nova = url_acess + endpoint_base + "/" + id
   result = requests.delete(url_nova)
   resposta = result.json()
   return resposta