---
title: H3_NUM_HEXAGONS (Lakehouse v1)
description: H3_NUM_HEXAGONS — gibt die Anzahl eindeutiger H3-Indizes bei der angegebenen Auflösung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

Gibt die Anzahl eindeutiger [H3](https://eng.uber.com/h3/)-Indizes bei der angegebenen Auflösung zurück.

## Analyze-Syntax

```python
func.h3_num_hexagons(res)
```

## Analyze-Beispiele

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## SQL-Syntax

```sql
H3_NUM_HEXAGONS(res)
```

## SQL-Beispiele

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
