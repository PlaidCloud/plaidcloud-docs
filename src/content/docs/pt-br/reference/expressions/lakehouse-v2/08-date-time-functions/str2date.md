---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — converte uma string em uma data usando uma string de formato. Alias de `STR_TO_DATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

Converte uma string em uma data usando uma string de formato. Alias de `STR_TO_DATE`.

## Sintaxe do Analyze

```python
func.str2date(<str>, <format>)
```

## Exemplos do Analyze

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
STR2DATE(<str>, <format>)
```

## Exemplos de SQL

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
