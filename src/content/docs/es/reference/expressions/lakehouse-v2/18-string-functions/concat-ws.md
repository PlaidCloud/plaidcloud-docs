---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS — Concatena cadenas con un separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

Concatena cadenas con un separador.

## Sintaxis de Analyze

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Ejemplos de Analyze

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## Ejemplos de SQL

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
