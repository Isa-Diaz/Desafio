
# 🏦 Sistema Bancário em Microserviços 🏦

##  Sobre o Projeto
Projeto desenvolvido como parte de um desafio de microserviços, com foco em regras bancárias simples, arquitetura limpa e testes unitários.

O sistema é dividido em dois microserviços:

### **Microserviço Acesso**
Responsável por:
- Validação de dados  
- Criação e atualização de clientes  
- Cálculo de score  
- Operações bancárias (saque e depósito)  
- Regras de cheque especial  
- Comunicação com o microserviço de armazenamento  

### **Microserviço Armazenamento**
Responsável por salvar e retornar os dados usando um banco SQLite.

---

## 🏗 Arquitetura

```
servidor/
│
├── acesso/             → Lógica e regras
│
├── micro_servico/      → Armazenamento (SQLite)
│
└── tests/              → Testes com pytest
```

---

## 🚩 Regras Principais

### **Score**
- Score nunca pode ser menor que zero  
- Quando o saldo é maior que zero, o score é calculado como:  
  **score = saldo × 0.1**

### **Cheque Especial (Limite)**
- O sistema permite uso de cheque especial  
- O limite é calculado como:  
  **limite = score × 3**

### **Operações**
- Depósito: soma ao saldo  
- Saque: permitido apenas se não ultrapassar saldo + limite  

---

## 🔗 Endpoints Importantes

### **Microserviço de Acesso**
```
POST   /clientes
GET    /clientes
GET    /clientes/<id>
PUT    /clientes/<id>
DELETE /clientes/<id>
GET    /clientes/<id>/score
POST   /clientes/<id>/operacao
```

### **Microserviço de Armazenamento**
- CRUD básico para clientes

---

## 🧪 Testes Unitários
Os testes utilizam **pytest**.

São testados:
- Validações  
- Cálculos  
- Serviços (com mock)

Para executar os testes:
*Antes de tudo, verifique se o nome do arquivo está como "servidor" e não "servidor -main" (por padrão o github baixa o arquivo com esse nome)

```
pytest -vv
```

---

## 🚀 Como Rodar o Projeto

### 1. Instalar dependências
```
pip install flask requests pytest pytest-cov
```

### 2. Iniciar microserviço de armazenamento
```
python3 -m micro_servico.controller
```

### 3. Iniciar microserviço de acesso
```
python3 -m acesso.controller
```
