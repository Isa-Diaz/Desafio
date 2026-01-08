from unittest.mock import patch
from servidor.acesso.service import (
    criar_cliente_service,
    atualizar_cliente_service,
    operacao_service
)


# TESTES criar_cliente_service

def test_criar_cliente_service_sucesso():
    dados = {
        "nome": "Ana",
        "telefone": "11999999999",
        "correntista": True,
        "saldo_cc": "100"
    }

    resposta_mock = {
        "id": 1,
        "nome": "Ana",
        "telefone": 11999999999,
        "correntista": True,
        "saldo_cc": 100.0,
        "score_credito": 10.0
    }

    with patch("servidor.acesso.service.criar_cliente") as mock_criar:
        mock_criar.return_value = resposta_mock

        resultado = criar_cliente_service(dados)

        mock_criar.assert_called_once()
        assert resultado == resposta_mock

def test_criar_cliente_service_dados_invalidos():
    dados_invalidos = {
        "telefone": "11999999999",
        "correntista": True,
        "saldo_cc": "100"
    }

    with patch("servidor.acesso.service.processar_dados") as mock_processar, \
         patch("servidor.acesso.service.criar_cliente") as mock_criar:

        mock_processar.return_value = "Erro simulado"

        resultado = criar_cliente_service(dados_invalidos)

        mock_processar.assert_called_once()
        mock_criar.assert_not_called()
        assert resultado == "Erro simulado"


# TESTES atualizar_cliente_service

def test_atualizar_cliente_service_sucesso():
    dados_atualizacao = {
        "nome": "Maria",
        "telefone": "11988887777",
        "correntista": False
    }

    cliente_mock = {
        "id": 1,
        "nome": "Ana",
        "telefone": 11999999999,
        "correntista": True,
        "score_credito": 10.0,
        "saldo_cc": 100.0
    }

    resposta_mock = {
        "id": 1,
        "nome": "Maria",
        "telefone": 11988887777,
        "correntista": False,
        "score_credito": 10.0,
        "saldo_cc": 100.0
    }

    with patch("servidor.acesso.service.buscar_cliente_por_id") as mock_buscar, \
         patch("servidor.acesso.service.atualizar_cliente") as mock_atualizar:

        mock_buscar.return_value = cliente_mock
        mock_atualizar.return_value = resposta_mock

        resultado = atualizar_cliente_service(1, dados_atualizacao)

        mock_buscar.assert_called_once_with(1)
        mock_atualizar.assert_called_once()
        assert resultado == resposta_mock

def test_atualizar_cliente_service_cliente_inexistente():
    with patch("servidor.acesso.service.buscar_cliente_por_id") as mock_buscar, \
         patch("servidor.acesso.service.atualizar_cliente") as mock_atualizar:

        mock_buscar.return_value = {"erro": "Cliente não encontrado"}

        resultado = atualizar_cliente_service(1, {"nome": "X"})

        mock_buscar.assert_called_once()
        mock_atualizar.assert_not_called()
        assert "erro" in resultado

def test_atualizar_cliente_service_telefone_invalido():
    cliente_mock = {
        "id": 1,
        "nome": "Ana",
        "telefone": 11999999999,
        "correntista": True,
        "score_credito": 10.0,
        "saldo_cc": 100.0
    }

    dados_invalidos = {"telefone": "abc"}

    with patch("servidor.acesso.service.buscar_cliente_por_id") as mock_buscar, \
         patch("servidor.acesso.service.atualizar_cliente") as mock_atualizar:

        mock_buscar.return_value = cliente_mock

        resultado = atualizar_cliente_service(1, dados_invalidos)

        mock_atualizar.assert_not_called()
        assert resultado == "Telefone inválido"


# TESTES operacao_service

def test_operacao_service_deposito_sucesso():
    cliente_mock = {
        "id": 1,
        "nome": "Isa",
        "telefone": 11999999999,
        "correntista": True,
        "score_credito": 10.0,
        "saldo_cc": 100.0
    }

    resposta_mock = {
        "id": 1,
        "nome": "Isa",
        "telefone": 11999999999,
        "correntista": True,
        "saldo_cc": 150.0,
        "score_credito": 15.0
    }

    with patch("servidor.acesso.service.buscar_cliente_por_id") as mock_buscar, \
         patch("servidor.acesso.service.atualizar_cliente") as mock_atualizar:

        mock_buscar.return_value = cliente_mock
        mock_atualizar.return_value = resposta_mock

        dados_operacao = {"tipo": "deposito", "valor": 50}
        resultado = operacao_service(1, dados_operacao)

        mock_buscar.assert_called_once_with(1)
        mock_atualizar.assert_called_once()
        assert resultado == resposta_mock

def test_operacao_service_limite_excedido():
    cliente_mock = {
        "id": 1,
        "nome": "Ana",
        "telefone": 11999999999,
        "correntista": True,
        "score_credito": 0.0,
        "saldo_cc": -200.0
    }

    with patch("servidor.acesso.service.buscar_cliente_por_id") as mock_buscar, \
         patch("servidor.acesso.service.atualizar_cliente") as mock_atualizar:

        mock_buscar.return_value = cliente_mock

        dados_operacao = {"tipo": "saque", "valor": 200}
        resultado = operacao_service(1, dados_operacao)

        mock_atualizar.assert_not_called()
        assert "limite" in resultado.lower()

def test_operacao_service_cliente_inexistente():
    with patch("servidor.acesso.service.buscar_cliente_por_id") as mock_buscar, \
         patch("servidor.acesso.service.atualizar_cliente") as mock_atualizar:

        mock_buscar.return_value = {"erro": "Cliente não encontrado"}

        resultado = operacao_service(1, {"tipo": "saque", "valor": 50})

        mock_atualizar.assert_not_called()
        assert "erro" in resultado