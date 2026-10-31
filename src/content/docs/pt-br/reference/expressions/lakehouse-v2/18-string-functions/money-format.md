---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT — formata um número como string de valor monetário, com vírgulas e duas casas decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

Formata um número como string de valor monetário, com vírgulas e duas casas decimais.

## Sintaxe do Analyze

```python
func.money_format(<num>)
```

## Exemplos do Analyze

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## Sintaxe SQL

```sql
MONEY_FORMAT(<num>)
```

## Exemplos de SQL

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
