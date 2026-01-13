# 🏦 Sistema Bancário em Microserviços 🏦

## Sobre o Projeto

Este projeto utiliza arquitetura de microserviços para simular um sistema bancário simples composto por dois serviços independentes:

### 🔷 Microserviço Acesso (porta 5001)

Responsável por:

* Validação de dados
* Regras bancárias
* Cálculo de score e limite
* Saque e depósito
* Comunicação com o microserviço de armazenamento

### 🔶 Microserviço Armazenamento (porta 5000)

Responsável por:

* Persistência dos dados
* CRUD completo em SQLite
* Respostas diretas ao microserviço de acesso

---

## Tecnologias Utilizadas

* Python
* Flask
* SQLite
* Requests
* Pytest

---

## Arquitetura do Projeto

```
servidor/
│
├── acesso/
│   ├── client.py
│   ├── controller.py
│   ├── service.py
│   └── __init__.py
│
├── micro_servico/
│   ├── controller.py
│   ├── repository.py
│   ├── database.py
│   └── __init__.py
│
└── tests/
```

---

## Fluxo Geral

### Criar Cliente

1. Requisição chega ao microserviço Acesso (5001)
2. Dados são validados
3. Score é calculado
4. Acesso envia dados ao Armazenamento (5000)
5. Armazenamento salva e devolve a resposta
6. Acesso retorna ao usuário

### Operações Bancárias

* Saque e depósito
* Regras de limite e cheque especial
* Recalculo de score após cada operação

---

## Regras de Negócio

### Score

```
score = saldo_cc × 0.1
```

### Cheque Especial

```
limite = score × 3
```

### Saque permitido se:

```
novo_saldo >= -limite
```

### Validações

* nome → string
* telefone → string numérica (10–11 dígitos)
* correntista → boolean
* saldo_cc → número ≥ 0

---

# 🔷 Microserviço de Acesso

**Base URL:** `http://127.0.0.1:5001`

### POST /clientes

Criar cliente

```json
{
  "nome": "Isa",
  "telefone": "11987654321",
  "correntista": true,
  "saldo_cc": 200
}
```

### GET /clientes

Listar todos

### GET /clientes/1

Buscar cliente

### PUT /clientes/1

Atualizar cliente

```json
{
  "nome": "Isabella",
  "telefone": "11999998888"
}
```

### DELETE /clientes/1

Remover cliente

### GET /clientes/1/score

Consultar score

### POST /clientes/1/operacao

Depósito:

```json
{
  "tipo": "deposito",
  "valor": 100
}
```

Saque:

```json
{
  "tipo": "saque",
  "valor": 50
}
```

---

# 🔶 Microserviço de Armazenamento

**Base URL:** `http://127.0.0.1:5000`

### Endpoints Internos

```
POST   /clientes
GET    /clientes
GET    /clientes/<id>
PUT    /clientes/<id>
DELETE /clientes/<id>
```

---

# 🚀 Como Executar

### Instalar dependências

```
pip install flask requests pytest pytest-cov
```

### Iniciar microserviço de armazenamento

```
python3 -m micro_servico.controller
```

### Iniciar microserviço de acesso

```
python3 -m acesso.controller
```

---

# 🧪 Testes

Executar:

```
pytest -vv
```

Cobertura inclui:

* Validações
* Score e limite
* Serviços
* Operações bancárias

---
