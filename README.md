# 🏦 Sistema Bancário em Microserviços🏦

## Sobre o Projeto

Este sistema simula um ambiente bancário utilizando **arquitetura de microserviços**, dividido em:

### 🔷 Microserviço Acesso (porta 5001)

Responsável por:

* Validação de dados
* Regras bancárias
* Cálculo de score
* Saque e depósito
* Comunicação com o microserviço de armazenamento
* Documentação Swagger integrada

### 🔶 Microserviço Armazenamento (porta 5000)

Responsável por:

* Persistência dos dados
* CRUD em SQLite
* Respostas diretas ao microserviço de acesso
* Documentação Swagger integrada

---

## Tecnologias Utilizadas

* Python
* Flask
* SQLite
* Requests
* Flasgger (Swagger)
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

### **Criar Cliente**

1. Requisição chega no microserviço **Acesso (5001)**
2. Dados são validados
3. Score é calculado
4. Acesso envia os dados ao microserviço **Armazenamento (5000)**
5. Armazenamento grava no banco
6. Acesso retorna a resposta ao usuário

### **Operações Bancárias**

* Saque e depósito
* Regras de limite e cheque especial
* Score recalculado após operações bancárias

---

## Regras de Negócio

### **Score**

```
score = saldo_cc × 0.1
```

### **Cheque especial**

```
limite = score × 3
```

### **Regra para saque**

```
novo_saldo >= -limite
```

### **Validações**

* nome → string
* telefone → string numérica de 10–11 dígitos
* correntista → boolean
* saldo_cc → número ≥ 0

---

# 🔷 Microserviço de Acesso (porta 5001)

Base URL:
`http://127.0.0.1:5001`

### **POST /clientes**

Criar cliente

```json
{
  "nome": "Isa",
  "telefone": "11987654321",
  "correntista": true,
  "saldo_cc": 200
}
```

### **GET /clientes**

Listar clientes

### **GET /clientes/1**

Buscar cliente por ID

### **PUT /clientes/1**

Atualizar cliente

```json
{
  "nome": "Isabella",
  "telefone": "11999998888",
  "correntista": true,
  "saldo_cc": 350
}
```

### **DELETE /clientes/1**

Excluir cliente

### **GET /clientes/1/score**

Consultar score

### **POST /clientes/1/operacao**

Operações bancárias

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

# 🔶 Microserviço de Armazenamento (porta 5000)

Base URL:
`http://127.0.0.1:5000`

### **POST /clientes**

Criar cliente

### **GET /clientes**

Listar clientes

### **GET /clientes/<id>**

Buscar cliente

### **PUT /clientes/<id>**

Atualizar cliente

### **DELETE /clientes/<id>**

Excluir cliente

---

# 🚀 Como Executar

### Instalar dependências

```
pip install flask flasgger requests pytest pytest-cov
```

### Iniciar microserviço de armazenamento (porta 5000)

```
python3 -m micro_servico.controller
```

### Iniciar microserviço de acesso (porta 5001)

```
python3 -m acesso.controller
```

---

# 📘 Documentação Swagger (Flasgger)

Ambos os microserviços têm documentação automática:

### 🔷 Swagger — Microserviço de Acesso

`http://127.0.0.1:5001/apidocs`

### 🔶 Swagger — Microserviço de Armazenamento

`http://127.0.0.1:5000/apidocs`

---

# 🧪 Testes

Executar testes:

```
pytest -vv
```

Cobrem:

* Validações
* Regras de score e limite
* Serviços
* Operações bancárias
* Fluxo completo entre microserviços

---
