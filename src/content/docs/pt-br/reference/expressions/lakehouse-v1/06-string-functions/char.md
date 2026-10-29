---
title: CHAR (Lakehouse v1)
description: CHAR — retorna o caractere correspondente a cada inteiro informado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

Retorna o caractere correspondente a cada inteiro informado.

## Sintaxe do Analyze

```python
func.char(N,...)
```

## Exemplos do Analyze

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## Sintaxe SQL

```sql
CHAR(N, ...)
```

## Argumentos

| Argumentos | Descrição         |
|-----------|-------------------|
| N         | Coluna numérica   |

## Tipo de retorno

`BINARY`

## Exemplos de SQL

Este exemplo mostra tanto o valor binário retornado quanto a representação em string.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
