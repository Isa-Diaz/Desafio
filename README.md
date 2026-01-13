---

# 🏦 Sistema Bancário em Microserviços 🏦

## Sobre o Projeto

Este projeto foi desenvolvido como um desafio utilizando arquitetura de microserviços para simular um sistema bancário simples.
Ele é dividido em dois serviços independentes:

### 🔷 Microserviço Acesso

Responsável por:

* Validação de dados
* Regras bancárias
* Cálculo de score e limite
* Operações (saque/deposito)
* Comunicação com o microserviço de armazenamento

### 🔶 Microserviço Armazenamento

Responsável por:

* Persistência dos dados em SQLite
* CRUD completo
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

1. Requisição chega no microserviço Acesso
2. Os dados são validados
3. O score é calculado
4. Os dados são enviados ao microserviço Armazenamento
5. A resposta final é retornada ao usuário

### Operações Bancárias

* Saque e depósito
* Regras de cheque especial
* Score recalculado após cada operação

---

## 🚨 Regras de Negócio

### Score

```
score = saldo × 0.1
```

Nunca pode ser menor que zero.

### Cheque Especial

```
limite = score × 3
```

### Saque

Permitido somente se:

```
novo_saldo >= -limite
```

### Validações Obrigatórias

* nome → string
* telefone → string numérica (10–11 dígitos)
* correntista → boolean
* saldo_cc → número ≥ 0

---

# 🔗 Endpoints e Exemplos de Requisição

---

# 🔷 Microserviço de Acesso

**Base URL:** `http://127.0.0.1:5001`

---

## 📌 Criar Cliente

### **POST /clientes**

### Corpo da requisição:

```json
{
  "nome": "Isa",
  "telefone": "11987654321",
  "correntista": true,
  "saldo_cc": 200
}
```

---

## 📌 Listar Clientes

### **GET /clientes**

---

## 📌 Buscar Cliente

### **GET /clientes/1**

---

## 📌 Atualizar Cliente

### **PUT /clientes/1**

### Exemplo:

```json
{
  "nome": "Isabella",
  "telefone": "11999998888"
}
```

---

## 📌 Deletar Cliente

### **DELETE /clientes/1**

---

## 📌 Consultar Score

### **GET /clientes/1/score**

---

## 📌 Operação (saque/deposito)

### **POST /clientes/1/operacao**

### Depósito:

```json
{
  "tipo": "deposito",
  "valor": 100
}
```

### Saque:

```json
{
  "tipo": "saque",
  "valor": 50
}
```

---

# 🔶 Microserviço de Armazenamento

**Base URL:** `http://127.0.0.1:5000`

### Endpoints:

```
POST   /clientes
GET    /clientes
GET    /clientes/<id>
PUT    /clientes/<id>
DELETE /clientes/<id>
```

---

# 🚀 Como Executar o Projeto

### 1️⃣ Instalar dependências

```
pip install flask requests pytest pytest-cov
```

### 2️⃣ Iniciar microserviço de armazenamento

```
python3 -m micro_servico.controller
```

### 3️⃣ Iniciar microserviço de acesso

```
python3 -m acesso.controller
```

---

# 🧪 Testes Unitários

### Rodar os testes:

```
pytest -vv
```

São testados:

* Validações
* Regras de score e limite
* Serviços
* Operações bancárias

---
