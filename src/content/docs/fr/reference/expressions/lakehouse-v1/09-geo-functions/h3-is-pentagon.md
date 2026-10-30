---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — vérifie si l'index H3 donné représente une cellule pentagonale.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

Vérifie si l'index [H3](https://eng.uber.com/h3/) donné représente une cellule pentagonale.

## Syntaxe Analyze

```python
func.h3_is_pentagon(h3)
```

## Exemples Analyze

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_IS_PENTAGON(h3)
```

## Exemples SQL

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
