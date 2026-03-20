# 🐍 PYTHON WORKSHOP — FÁBRICA DE SOFTWARE

Repositório de estudos do workshop de Python com foco em Back-End, cobrindo desde os fundamentos da linguagem até Programação Orientada a Objetos e boas práticas de desenvolvimento.

---

## 📋 Sumário

1. [O que é Python?](#1-o-que-é-python)
2. [Variáveis e Tipos de Dados](#2-variáveis-e-tipos-de-dados)
3. [Entrada e Saída de Dados](#3-entrada-e-saída-de-dados)
4. [Operadores Matemáticos](#4-operadores-matemáticos)
5. [Estruturas Condicionais](#5-estruturas-condicionais)
6. [Estruturas de Repetição](#6-estruturas-de-repetição)
7. [Listas, Tuplas, Dicionários e Conjuntos](#7-listas-tuplas-dicionários-e-conjuntos)
8. [Funções](#8-funções)
9. [Programação Orientada a Objetos (POO)](#9-programação-orientada-a-objetos-poo)
10. [Módulos e Bibliotecas](#10-módulos-e-bibliotecas)
11. [Constantes em Python](#11-constantes-em-python)
12. [Tipos Comuns de Erros](#12-tipos-comuns-de-erros)
13. [Convenções de Nomenclatura (PEP 8)](#13-convenções-de-nomenclatura-pep-8)
14. [Ambiente Virtual (venv)](#14-ambiente-virtual-venv)

---

## 1. O que é Python?

Python é uma linguagem simples, versátil e de sintaxe próxima à linguagem humana. Amplamente utilizada em desenvolvimento web, automação, ciência de dados e inteligência artificial.

---

## 2. Variáveis e Tipos de Dados

Variáveis armazenam informações. Python identifica o tipo automaticamente — não é necessário declará-lo.

```python
nome   = "Maria"  # str   — texto
idade  = 25       # int   — número inteiro
altura = 1.70     # float — número decimal
ativo  = True     # bool  — verdadeiro/falso
```

---

## 3. Entrada e Saída de Dados

`input()` captura dados do usuário (sempre retorna `string`) e `print()` os exibe. Converta o tipo quando necessário.

```python
nome   = input("Digite seu nome: ")
idade  = int(input("Digite sua idade: "))     # str → int
altura = float(input("Digite sua altura: "))  # str → float
print(f"Olá, {nome}! Você tem {idade} anos.")
```

---

## 4. Operadores Matemáticos

| Operador | Operação        | Resultado      |
|----------|-----------------|----------------|
| `+` `-` `*` `/` | Básicos  | `5 / 2` → `2.5` |
| `//`     | Divisão inteira | `5 // 2` → `2` |
| `%`      | Resto (módulo)  | `5 % 2` → `1`  |
| `**`     | Potenciação     | `2 ** 3` → `8` |

---

## 5. Estruturas Condicionais

Tomam decisões com base em condições (`True`/`False`) usando `if`, `elif` e `else`.

```python
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
```

---

## 6. Estruturas de Repetição

- **`for`** — itera sobre uma sequência com número de repetições definido.
- **`while`** — repete enquanto uma condição for verdadeira.

```python
for i in range(5):   # 0, 1, 2, 3, 4
    print(i)

contador = 0
while contador < 5:
    contador += 1
```

---

## 7. Listas, Tuplas, Dicionários e Conjuntos

| Estrutura      | Mutável | Ordenado | Duplicados | Uso principal                |
|----------------|---------|----------|------------|------------------------------|
| **Lista** `[]` | ✅      | ✅       | ✅         | Coleção modificável          |
| **Tupla** `()` | ❌      | ✅       | ✅         | Dados fixos e imutáveis      |
| **Dict** `{}`  | ✅      | ✅*      | ❌ chaves  | Dados em formato chave-valor |
| **Set** `{}`   | ✅      | ❌       | ❌         | Valores únicos, sem índice   |

> *Dicionários mantêm ordem de inserção a partir do Python 3.7

```python
lista = [1, 2, 3]
tupla = (1, 2, 3)
dicio = {"nome": "Ana", "idade": 25}
conj  = {1, 2, 3}
```

---

## 8. Funções

Blocos de código reutilizáveis definidos com `def`. Podem receber parâmetros e retornar valores com `return`.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

def soma(a, b):
    return a + b

saudacao("Isaac")  # Olá, Isaac!
print(soma(2, 5))  # 7
```

---

## 9. Programação Orientada a Objetos (POO)

A POO organiza o código em **classes** (moldes) e **objetos** (instâncias), agrupando atributos e comportamentos relacionados.

```python
class Pessoa:
    def __init__(self, nome, idade):  # Construtor
        self.nome  = nome
        self.idade = idade

    def apresentar(self):
        print(f"Sou {self.nome}, {self.idade} anos.")

p = Pessoa("Ana", 25)
p.apresentar()  # Sou Ana, 25 anos.
```

> **Pilares da POO:** Encapsulamento · Herança · Polimorfismo · Abstração

---

## 10. Módulos e Bibliotecas

Python possui módulos nativos prontos para uso e bibliotecas externas instaláveis via `pip`.

```python
import math;     print(math.sqrt(16))           # 4.0
import random;   print(random.randint(1, 10))    # Número aleatório
import datetime; print(datetime.datetime.now())  # Data/hora atual
```

| Biblioteca   | Função                   | Instalação               |
|--------------|--------------------------|--------------------------|
| `requests`   | Requisições HTTP         | `pip install requests`   |
| `numpy`      | Arrays numéricos         | `pip install numpy`      |
| `pandas`     | Análise de dados         | `pip install pandas`     |
| `matplotlib` | Gráficos e visualizações | `pip install matplotlib` |

---

## 11. Constantes em Python

Python não possui constantes nativas. Por convenção do PEP 8, usamos **LETRAS_MAIÚSCULAS** para indicar que o valor não deve ser alterado.

```python
PI             = 3.14159
GRAVIDADE      = 9.8
MAX_TENTATIVAS = 3
```

---

## 12. Tipos Comuns de Erros

Conhecer os erros mais frequentes agiliza muito o processo de depuração.

| Erro                | Causa                                    | Exemplo                              |
|---------------------|------------------------------------------|--------------------------------------|
| `SyntaxError`       | Erro de sintaxe no código                | `print("Olá"` — aspas não fechadas   |
| `IndentationError`  | Indentação incorreta                     | Bloco `if` sem recuo                 |
| `NameError`         | Variável usada antes de ser definida     | `print(nome)` sem definir `nome`     |
| `TypeError`         | Tipos incompatíveis na operação          | `3 + "a"`                            |
| `IndexError`        | Índice fora do intervalo da lista/tupla  | `lista[10]` em lista de 5 itens      |
| `KeyError`          | Chave inexistente no dicionário          | `dados["idade"]` sem essa chave      |
| `ZeroDivisionError` | Divisão por zero                         | `10 / 0`                             |
| `ValueError`        | Valor incompatível com a operação        | `int("abc")`                         |

---

## 13. Convenções de Nomenclatura (PEP 8)

O **PEP 8** é o guia oficial de boas práticas para código Python legível e padronizado.

| Elemento         | Convenção                   | Exemplo                  |
|------------------|-----------------------------|--------------------------|
| Variáveis        | `snake_case`                | `idade_usuario = 25`     |
| Constantes       | `MAIÚSCULAS_COM_UNDERSCORE` | `PI = 3.14159`           |
| Funções          | `snake_case`                | `def calcular_media():`  |
| Classes          | `PascalCase`                | `class ContaBancaria:`   |
| Métodos privados | Prefixo `_`                 | `def _calcular_taxa():`  |
| Arquivos         | `snake_case`                | `processador_dados.py`   |

---

## 14. Ambiente Virtual (venv)

Isola as dependências do projeto, evitando conflitos com outras versões instaladas no sistema.

```powershell
# Criar o ambiente
python -m venv venv

# Ativar (Windows PowerShell)
venv\Scripts\Activate

# Se der erro de permissão, execute antes:
Set-ExecutionPolicy Unrestricted -Scope Process
```

---

## 🚀 Como Executar

```bash
# Clone o repositório e acesse a pasta
git clone https://github.com/Agamedesrmeira/Python-POO-Bibliotecas.git
cd Python-POO-Bibliotecas

# Crie e ative o ambiente virtual (Windows)
python -m venv venv
venv\Scripts\Activate

# Execute os scripts
python "Dia 01/script.py"
```

---

*Fábrica de Software — Back-End com Python*
