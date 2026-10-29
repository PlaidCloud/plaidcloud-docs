---
title: REPEAT (Lakehouse v2)
description: REPEAT — wiederholt eine Zeichenfolge in der angegebenen Anzahl.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

Wiederholt eine Zeichenfolge in der angegebenen Anzahl.

## Analyze-Syntax

```python
func.repeat(<str>, <n>)
```

## Analyze-Beispiele

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## SQL-Syntax

```sql
REPEAT(<str>, <n>)
```

## SQL-Beispiele

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
