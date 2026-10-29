---
title: ASCII (Lakehouse v2)
description: ASCII — Retorna o código ASCII do primeiro caractere de uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

Retorna o código ASCII do primeiro caractere de uma string.

## Sintaxe do Analyze

```python
func.ascii(<str>)
```

## Exemplos do Analyze

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## Sintaxe SQL

```sql
ASCII(<str>)
```

## Exemplos de SQL

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
