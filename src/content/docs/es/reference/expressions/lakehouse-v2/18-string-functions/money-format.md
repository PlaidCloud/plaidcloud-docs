---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT — Da formato a un número como una cadena de moneda con comas y dos decimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

Da formato a un número como una cadena de moneda con comas y dos decimales.

## Sintaxis de Analyze

```python
func.money_format(<num>)
```

## Ejemplos de Analyze

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## Sintaxis de SQL

```sql
MONEY_FORMAT(<num>)
```

## Ejemplos de SQL

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
