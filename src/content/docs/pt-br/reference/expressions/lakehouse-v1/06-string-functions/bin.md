---
title: BIN (Lakehouse v1)
description: BIN — retorna uma representação em string do valor binário de N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

Retorna uma representação em string do valor binário de N.

## Sintaxe do Analyze

```python
func.bin(<expr>)
```

## Exemplos do Analyze

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## Sintaxe SQL

```sql
BIN(<expr>)
```

## Argumentos

| Argumentos | Descrição   |
|-----------|-------------|
| `<expr>`  | O número.   |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
