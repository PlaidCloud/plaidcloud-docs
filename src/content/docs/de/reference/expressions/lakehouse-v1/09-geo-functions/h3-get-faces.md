---
title: H3_GET_FACES (Lakehouse v1)
description: H3_GET_FACES — ermittelt alle Ikosaederflächen, die vom angegebenen H3-Index geschnitten werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

Ermittelt alle Ikosaederflächen, die vom angegebenen [H3](https://eng.uber.com/h3/)-Index geschnitten werden. Die Flächen werden als ganze Zahlen von 0 bis 19 dargestellt.

## Analyze-Syntax

```python
func.h3_get_faces(h3)
```

## Analyze-Beispiele

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_GET_FACES(h3)
```

## SQL-Beispiele

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
