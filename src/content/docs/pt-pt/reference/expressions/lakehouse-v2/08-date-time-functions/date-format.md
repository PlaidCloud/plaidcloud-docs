---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT — formata um valor de data ou data e hora de acordo com uma cadeia de formato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

Formata um valor de data ou data e hora de acordo com uma cadeia de formato.

## Sintaxe do Analyze

```python
func.date_format(<date>, <format>)
```

## Exemplos do Analyze

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DATE_FORMAT(<date>, <format>)
```

## Exemplos SQL

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
