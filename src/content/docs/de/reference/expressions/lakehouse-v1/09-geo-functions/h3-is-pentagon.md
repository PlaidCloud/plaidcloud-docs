---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — prüft, ob der angegebene H3-Index eine fünfeckige Zelle darstellt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

Prüft, ob der angegebene [H3](https://eng.uber.com/h3/)-Index eine fünfeckige Zelle darstellt.

## Analyze-Syntax

```python
func.h3_is_pentagon(h3)
```

## Analyze-Beispiele

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_IS_PENTAGON(h3)
```

## SQL-Beispiele

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
