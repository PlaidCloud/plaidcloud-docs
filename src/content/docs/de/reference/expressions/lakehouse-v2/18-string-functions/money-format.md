---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT — formatiert eine Zahl als Währungszeichenfolge mit Kommas und zwei Dezimalstellen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

Formatiert eine Zahl als Währungszeichenfolge mit Kommas und zwei Dezimalstellen.

## Analyze-Syntax

```python
func.money_format(<num>)
```

## Analyze-Beispiele

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## SQL-Syntax

```sql
MONEY_FORMAT(<num>)
```

## SQL-Beispiele

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
