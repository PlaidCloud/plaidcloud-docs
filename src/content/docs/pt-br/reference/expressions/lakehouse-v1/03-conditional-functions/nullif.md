---
title: NULLIF (Lakehouse v1)
description: NULLIF — retorna NULL se duas expressões forem iguais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

Retorna NULL se duas expressões forem iguais. Caso contrário, retorna expr1. Elas devem ter o mesmo tipo de dados.

## Sintaxe do Analyze

```python
func.nullif(<expr1>, <expr2>)
```

## Exemplos do Analyze

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
NULLIF(<expr1>, <expr2>)
```

## Exemplos de SQL

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
