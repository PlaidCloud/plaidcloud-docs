---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — convierte una cadena en una fecha mediante una cadena de formato. Alias de `STR_TO_DATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

Convierte una cadena en una fecha mediante una cadena de formato. Alias de `STR_TO_DATE`.

## Sintaxis de Analyze

```python
func.str2date(<str>, <format>)
```

## Ejemplos de Analyze

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
STR2DATE(<str>, <format>)
```

## Ejemplos de SQL

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
