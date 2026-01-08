from servidor.acesso.service import validar_dados, validar_operacao


# TESTES validar_dados

def test_validar_dados_valido():
    dados = {
        "nome": "Ana",
        "telefone": "11999999999",
        "correntista": True,
        "saldo_cc": "100"
    }

    assert validar_dados(dados) is None

def test_validar_dados_nome_faltando():
    dados = {
        "telefone": "11999999999",
        "correntista": True,
        "saldo_cc": "100"
    }

    resultado = validar_dados(dados)

    assert isinstance(resultado, str)
    assert "nome" in resultado.lower()

def test_validar_dados_telefone_invalido_formato():
    dados = {
        "nome": "Ana",
        "telefone": "abc",
        "correntista": True,
        "saldo_cc": "100"
    }

    resultado = validar_dados(dados)

    assert isinstance(resultado, str)
    assert "telefone" in resultado.lower()

def test_validar_dados_correntista_invalido():
    dados = {
        "nome": "Ana",
        "telefone": "11999999999",
        "correntista": "sim",
        "saldo_cc": "100"
    }

    resultado = validar_dados(dados)

    assert isinstance(resultado, str)
    assert "correntista" in resultado.lower()


# TESTES validar_operacao

def test_validar_operacao_valida():
    dados = {"tipo": "saque", "valor": 50}
    assert validar_operacao(dados) is None

def test_validar_operacao_tipo_invalido():
    dados = {"tipo": "pix", "valor": 50}

    resultado = validar_operacao(dados)

    assert isinstance(resultado, str)
    assert "tipo" in resultado.lower()

def test_validar_operacao_valor_negativo():
    dados = {"tipo": "saque", "valor": -20}

    resultado = validar_operacao(dados)

    assert isinstance(resultado, str)
    assert "valor" in resultado.lower()

def test_validar_operacao_valor_nao_numerico():
    dados = {"tipo": "deposito", "valor": "abc"}

    resultado = validar_operacao(dados)

    assert isinstance(resultado, str)
    assert "valor" in resultado.lower()
