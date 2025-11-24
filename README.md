---
title: "Vaga estágio dti digital"
source: "https://chatgpt.com/c/691e2d72-ad38-8331-9f6a-4f9a6b639675"
author:
  - "[[ChatGPT]]"
published:
created: 2025-11-23
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
```
# 🐾 Pet Feeding — CRUD Application (Estágio Dev dti digital)

Este projeto implementa um CRUD simples para gerenciar registros de alimentação de pets, conforme solicitado no case técnico do processo seletivo para estágio em desenvolvimento da **dti digital**.

A aplicação segue uma **arquitetura em camadas** (Model → Repository → Service → Controller) e utiliza **SQLite** como banco de dados, persistido localmente através do SQLAlchemy.

---

## 📚 Sumário
- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Modelo da Tabela](#modelo-da-tabela)
- [DDL da Tabela (Arquivo .sql)](#ddl-da-tabela-arquivo-sql)
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Fluxo do Usuário](#fluxo-do-usuário)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Decisões de Implementação](#decisões-de-implementação)
- [Possíveis Melhorias Futuras](#possíveis-melhorias-futuras)

---

## 📌 Descrição do Projeto

O objetivo é criar uma aplicação de console capaz de:

- Inserir registros de alimentação de pets  
- Listar todos os registros  
- Buscar por ID  
- Atualizar registros existentes  
- Deletar registros  

Cada ação é processada dentro de uma camada de **serviço**, que faz validações e orquestra a comunicação com a camada **repository**, responsável apenas pelas operações de banco de dados.

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Uso |
|-----------|-----|
| **Python 3.10+** | Linguagem principal |
| **SQLite3** | Banco de dados leve e embutido |
| **SQLAlchemy ORM** | Mapeamento objeto-relacional e criação do esquema |
| **Context Manager para sessões** | Controle transacional por operação |
| **Arquitetura MVC simplificada (CLI)** | Separação clara das responsabilidades |

---

## 🏛 Arquitetura do Projeto

A aplicação foi organizada seguindo boas práticas de backend:
```

main.py → Controller (entrada do usuário)  
service.py → Regras de negócio  
repository.py → Acesso ao banco (SQLAlchemy)  
model.py → Entidades e schema ORM  
database.py → Engine, sessão e init\_db()

```
### ✔ Responsabilidades

**Model:**  
Define o formato dos dados, validações estruturais e mapeamento ORM.

**Repository:**  
Contém métodos que conversam diretamente com o banco.  
Não possui regras de negócio ou prints.  
Cada método executa operações como \`insert\`, \`select\`, \`update\`, \`delete\`.

**Service:**  
Valida dados, decide fluxos, traduz mensagens, coordena repository.  
Não contém SQL ou sessões.

**Controller (main):**  
Exibe menu, lê inputs, chama métodos do service e exibe resultados.

---

## 🐾 Modelo da Tabela

A entidade **PetFeeding** modela um registro de alimentação contendo:

- **id** (int, PK)
- **pet_name** (string até 30 chars, obrigatório)
- **person_name** (string, opcional)
- **amount_servings** (float > 0)
- **time_feeding** (timestamp, default now)

Código ORM utilizado:

\`\`\`python
from datetime import datetime
from sqlalchemy import String, func, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    ...

class PetFeeding(Base):
    __tablename__ = 'PetFeeding'

    id: Mapped[int] = mapped_column(primary_key=True)
    pet_name: Mapped[str] = mapped_column(String(30), nullable=False)
    person_name: Mapped[str]
    amount_servings: Mapped[float] = mapped_column(
        CheckConstraint('amount_serving > 0')
    )
    time_feeding: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
```

---

## 🧾 DDL da Tabela (Arquivo .sql)

O case exige um arquivo `.sql` contendo a criação da tabela.  
Abaixo está a versão equivalente ao modelo acima:

```
CREATE TABLE PetFeeding (
    id INTEGER PRIMARY KEY,
    pet_name TEXT NOT NULL,
    person_name TEXT,
    amount_servings REAL CHECK (amount_servings > 0),
    time_feeding DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

Este arquivo está incluído em:  
`/sql/create_table.sql`

---

## ⚙ Funcionalidades Implementadas

### ✔ CRUD Completo

- **Listar todas as alimentações**
- **Buscar por ID**
- **Criar novo registro**
- **Atualizar registro existente**
- **Deletar por ID**

### ✔ Outras características

- Transações garantidas por context manager de sessão
- Separação clara de responsabilidades
- Mensagens tratadas no serviço
- Validações simples (campos obrigatórios, valores positivos)
- Tabela criada automaticamente se não existir (`init_db()`)

---

## ▶ Como Rodar o Projeto

### 1\. Criar ambiente virtual (opcional)

```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 2\. Instalar dependências

```
pip install -r requirements.txt
```

### 3\. Executar o programa

```
python main.py
```

O arquivo `app.db` será criado automaticamente na primeira execução.

---

## 🧭 Fluxo do Usuário

Ao iniciar, o usuário verá um menu como:

```
##############################
---------PET FEEDING---------
##############################

1- List Feedings
2- Search by ID
3- Add New Feeding
4- Update Entry
5- Delete Entry
x- Exit App
```

Cada ação chama um método no serviço, que processa dados e retorna mensagens amigáveis.

---

## 📁 Estrutura de Diretórios

```
project/
│
├── app/
│   ├── model.py
│   ├── repository.py
│   ├── service.py
│   ├── database.py
│
├── sql/
│   └── create_table.sql
│
├── main.py
└── README.md
```