---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS — concatena strings usando um separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

Concatena strings usando um separador.

## Sintaxe do Analyze

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Exemplos do Analyze

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## Exemplos de SQL

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
