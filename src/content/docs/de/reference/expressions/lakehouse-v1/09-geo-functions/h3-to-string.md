---
title: H3_TO_STRING (Lakehouse v1)
description: H3_TO_STRING — wandelt die Darstellung des angegebenen H3-Index in die Zeichenfolgendarstellung um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

Wandelt die Darstellung des angegebenen [H3](https://eng.uber.com/h3/)-Index in die Zeichenfolgendarstellung um.

## Analyze-Syntax

```python
func.h3_to_string(h3)
```

## Analyze-Beispiele

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_TO_STRING(h3)
```

## SQL-Beispiele

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
