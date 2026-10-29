---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT — met un nombre en forme de chaîne monétaire, avec des virgules et deux décimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

Met un nombre en forme de chaîne monétaire, avec des virgules et deux décimales.

## Syntaxe Analyze

```python
func.money_format(<num>)
```

## Exemples Analyze

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## Syntaxe SQL

```sql
MONEY_FORMAT(<num>)
```

## Exemples SQL

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
