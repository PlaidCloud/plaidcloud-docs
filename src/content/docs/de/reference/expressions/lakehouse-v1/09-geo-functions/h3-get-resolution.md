---
title: H3_GET_RESOLUTION (Lakehouse v1)
description: H3_GET_RESOLUTION — gibt die Auflösung des angegebenen H3-Index zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-resolution.md
---

Gibt die Auflösung des angegebenen [H3](https://eng.uber.com/h3/)-Index zurück.

## Analyze-Syntax

```python
func.h3_get_resolution(h3)
```

## Analyze-Beispiele

```python
func.h3_get_resolution(644325524701193974)

┌────────────────────────────────────────────┐
│ func.h3_get_resolution(644325524701193974) │
├────────────────────────────────────────────┤
│                                         15 │
└────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_GET_RESOLUTION(h3)
```

## SQL-Beispiele

```sql
SELECT H3_GET_RESOLUTION(644325524701193974);

┌───────────────────────────────────────┐
│ h3_get_resolution(644325524701193974) │
├───────────────────────────────────────┤
│                                    15 │
└───────────────────────────────────────┘
```
