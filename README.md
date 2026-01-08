 🏦 Sistema Bancário em Microserviços 🏦
=====================================================
 Sobre o Projeto

Projeto criado como parte de um desafio de microserviços, com foco em regras bancárias simples, arquitetura limpa e testes unitários.
Ele possui dois serviços separados:

    Microserviço Acesso
Responsável pela lógica do sistema, como:

validação de dados
criação e atualização de clientes
cálculo de score
operações bancárias (saque e depósito)
regras de cheque especial
comunicação com o microserviço de banco de dados

    Microserviço Armazenamento
Responsável por salvar e buscar os dados no banco (SQLite).

---
    Arquitetura (resumo)

servidor/
│
├── acesso/             → Lógica e regras
│
├── micro_servico/      → Armazenamento (SQLite)
│
└── tests/              → Testes com pytest


---
🚩 Regras Principais

    Score:
Score não pode ser um número inferior a zero
Enquanto saldo for mais que zero multiplicaremos saldo por 0.1 para obter o score


    Limite (cheque especial):
Assim como bancos reais é possivel usar cheque especial, no nosso sistema não é diferente, o calculo é baseado no score multiplicado por 3


    Operações:
Depósito: soma ao saldo
Saque: só permitido se não ultrapassar o limite do cheque especial

---
    Endpoints Importantes
Microserviço Acesso
POST /clientes
GET /clientes
GET /clientes/<id>
PUT /clientes/<id>
DELETE /clientes/<id>
GET /clientes/<id>/score
POST /clientes/<id>/operacao
Microserviço Armazenamento
Possui CRUD básico.
---
🧪 Testes Unitários
Para esse teste foi usado o pytest (É importante que baixe a biblioteca )
validações
cálculos
serviços (com mock)
Rodar testes:

    Para verificar é só rodar o codigo abaixo no seu terminal:
pytest -vv
---

    Como rodar o projeto
1. Instalar dependências:
pip install flask requests pytest pytest-cov


2. Rodar microserviço de armazenamento:
cd micro_servico
python3 controller.py


3. Rodar microserviço de acesso:
cd acesso
python3 controller.py