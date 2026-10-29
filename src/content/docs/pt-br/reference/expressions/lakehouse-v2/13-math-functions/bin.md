---
title: BIN (Lakehouse v2)
description: BIN — retorna a representação em string binária de um inteiro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

Retorna a representação em string binária de um inteiro.

## Sintaxe do Analyze

```python
func.bin(<x>)
```

## Exemplos do Analyze

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## Sintaxe SQL

```sql
BIN(<x>)
```

## Exemplos de SQL

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
