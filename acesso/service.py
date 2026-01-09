from .client import criar_cliente, atualizar_cliente, buscar_cliente_por_id

def validar_dados(dados):

    if dados.get("nome") is None:
        return "O campo nome é obrigatorio"
    
    if dados.get("telefone") is None:
        return "O campo telefone é obrigatorio"

    if dados.get("correntista") is None:
        return "O campo correntista é obrigatorio"
    
    if not isinstance(dados.get("nome"), str):
        return "Nome inválido"
    if dados.get("nome") == "":
        return "Nome não pode estar vazio"

    if not isinstance(dados.get("correntista"), bool):
        return "Correntista inválido"

    if not isinstance(dados.get("telefone"), str):
        return "Telefone inválido"
    if dados.get("telefone") == "":
        return "Telefone não pode estar vazio"

    telefone = dados["telefone"]   
    if len(telefone) < 10 or len(telefone) > 11:
        return "Telefone deve ter entre 10 e 11 dígitos"

    try:
        int(telefone)
    except:
        return "Telefone deve conter apenas números"

    return None

def calcular_score(saldo):
    if saldo > 0:
        score_credito = saldo * 0.1
        return score_credito
    elif saldo <= 0:
        score_credito = 0
        return score_credito
     
def processar_dados(dados):
    # Valida nome, telefone, correntista
    result = validar_dados(dados)
    if result is not None:
        return result

    # Valida saldo (somente POST)
    saldo_str = dados.get("saldo_cc")
    if saldo_str is None:
        return "O campo saldo_cc é obrigatório"

    try:
        saldo_cc = float(saldo_str)
    except:
        return "Saldo inválido. Deve ser número."

    if saldo_cc < 0:
        return "Saldo não pode ser negativo"

    # Converter telefone
    try:
        telefone = int(dados["telefone"])
    except:
        return "Telefone inválido. Deve conter apenas números."

    # Calcular score
    score_credito = calcular_score(saldo_cc)

    # Montar dados finais
    novo_dados = {
        "nome": dados["nome"],
        "telefone": telefone,
        "correntista": dados["correntista"],
        "saldo_cc": saldo_cc,
        "score_credito": score_credito
    }

    return novo_dados

def criar_cliente_service(dados):
    result = processar_dados(dados)
    if type(result) is str:
        return result
    else:
        return criar_cliente(result)
    
def atualizar_cliente_service(id, dados):
    cliente = buscar_cliente_por_id(id)
    if "erro" in cliente:
        return cliente

    nome = dados.get("nome", cliente["nome"])
    telefone = dados.get("telefone", cliente["telefone"])
    try:
        telefone = int(telefone)
    except:
        return "Telefone inválido"
    correntista = dados.get("correntista", cliente["correntista"])

    saldo = cliente["saldo_cc"]
    score = cliente["score_credito"]

    novos_dados = {
        "nome": nome,
        "telefone": telefone,
        "correntista": correntista,
        "saldo_cc": saldo,
        "score_credito": score
    }

    return atualizar_cliente(id, novos_dados)

def calcular_novo_saldo(saldo_atual, tipo, valor):
    if tipo == "deposito":
        return saldo_atual + valor
    elif tipo == "saque":
        return saldo_atual - valor

def calcular_limite(score):
    return score * 3

def validar_operacao(dados):
    tipo = dados.get("tipo")
    valor = dados.get("valor")

    if tipo is None:
        return "O campo tipo é obrigatório"

    if tipo not in ["saque", "deposito"]:
        return "Tipo de operação inválido. Use 'saque' ou 'deposito'."

    if valor is None:
        return "O campo valor é obrigatório"

    try:
        valor = float(valor)
    except:
        return "Valor deve ser um número"

    if valor <= 0:
        return "Valor deve ser maior que zero"

    return None

def operacao_service(id, dados):
    result = validar_operacao(dados)
    if result:
        return result

    cliente = buscar_cliente_por_id(id)
    if "erro" in cliente:
        return cliente

    tipo = dados["tipo"]
    valor = float(dados["valor"])
    saldo_atual = cliente["saldo_cc"]

    novo_saldo = calcular_novo_saldo(saldo_atual, tipo, valor)

    novo_score = calcular_score(novo_saldo)

    limite = calcular_limite(novo_score)

    if novo_saldo < -limite:
        return "Saldo excede o limite do cheque especial"

    novos_dados = {
        "nome": cliente["nome"],
        "telefone": cliente["telefone"],
        "correntista": cliente["correntista"],
        "saldo_cc": novo_saldo,
        "score_credito": novo_score
    }
    resposta = atualizar_cliente(id, novos_dados)
    return resposta
