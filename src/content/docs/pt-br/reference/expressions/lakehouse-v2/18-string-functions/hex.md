---
title: HEX (Lakehouse v2)
description: HEX — Retorna a representação hexadecimal de uma string ou de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

Retorna a representação hexadecimal de uma string ou de um número.

## Sintaxe do Analyze

```python
func.hex(<expr>)
```

## Exemplos do Analyze

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## Sintaxe SQL

```sql
HEX(<expr>)
```

## Exemplos de SQL

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
