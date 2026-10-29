---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — comprueba si el índice H3 dado representa una celda pentagonal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

Comprueba si el índice [H3](https://eng.uber.com/h3/) dado representa una celda pentagonal. 

## Sintaxis de Analyze

```python
func.h3_is_pentagon(h3)
```

## Ejemplos de Analyze

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_IS_PENTAGON(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
