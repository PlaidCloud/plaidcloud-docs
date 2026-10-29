---
title: STRING_TO_H3 (Lakehouse v1)
description: STRING_TO_H3 — wandelt die Zeichenfolgendarstellung in die H3-Darstellung (uint64) um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/string-to-h3.md
---

Wandelt die Zeichenfolgendarstellung in die [H3](https://eng.uber.com/h3/)-Darstellung (uint64) um.

## Analyze-Syntax

```python
func.string_to_h3(h3)
```

## Analyze-Beispiele

```python
func.string_to_h3('8d11aa6a38826ff')

┌──────────────────────────────────────┐
│ func.string_to_h3('8d11aa6a38826ff') │
├──────────────────────────────────────┤
│                   635318325446452991 │
└──────────────────────────────────────┘
```

## SQL-Syntax

```sql
STRING_TO_H3(h3)
```

## SQL-Beispiele

```sql
SELECT STRING_TO_H3('8d11aa6a38826ff');

┌─────────────────────────────────┐
│ string_to_h3('8d11aa6a38826ff') │
├─────────────────────────────────┤
│              635318325446452991 │
└─────────────────────────────────┘
```
