---
title: NULLIF (Lakehouse v2)
description: NULLIF — retorna NULL se duas expressões forem iguais; caso contrário, retorna a primeira expressão.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

Retorna NULL se duas expressões forem iguais; caso contrário, retorna a primeira expressão.

## Sintaxe do Analyze

```python
func.nullif(get_column(table, 'value'), 0)
```

## Exemplos do Analyze

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## Sintaxe SQL

```sql
NULLIF(<value>, 0)
```

## Exemplos SQL

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
