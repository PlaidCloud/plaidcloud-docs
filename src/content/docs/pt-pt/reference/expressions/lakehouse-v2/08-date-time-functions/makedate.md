---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE — cria uma data a partir de um ano e de um valor de dia do ano.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

Cria uma data a partir de um ano e de um valor de dia do ano.

## Sintaxe do Analyze

```python
func.makedate(<year>, <dayofyear>)
```

## Exemplos do Analyze

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## Sintaxe SQL

```sql
MAKEDATE(<year>, <dayofyear>)
```

## Exemplos SQL

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
