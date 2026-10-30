---
title: BIN (Lakehouse v2)
description: BIN — devolve a representação binária, em cadeia de caracteres, de um número inteiro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

Devolve a representação binária, em cadeia de caracteres, de um número inteiro.

## Sintaxe de Analyze

```python
func.bin(<x>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
