---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — converte uma cadeia de caracteres numa data através de uma cadeia de formato. Alias de `STR_TO_DATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

Converte uma cadeia de caracteres numa data através de uma cadeia de formato. Alias de `STR_TO_DATE`.

## Sintaxe de Analyze

```python
func.str2date(<str>, <format>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
