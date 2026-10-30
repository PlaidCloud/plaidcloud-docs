---
title: H3_LINE (Lakehouse v1)
description: H3_LINE — renvoie la ligne d'index entre les deux index H3 donnés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-line.md
---

Renvoie la ligne d'index entre les deux index [H3](https://eng.uber.com/h3/) donnés.

## Syntaxe Analyze

```python
func.h3_line(h3, a_h3)
```

## Exemples Analyze

```python
func.h3_line(599119489002373119, 599119491149856767)

┌──────────────────────────────────────────────────────┐
│ func.h3_line(599119489002373119, 599119491149856767) │
├──────────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]              │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_LINE(h3, a_h3)
```

## Exemples SQL

```sql
SELECT H3_LINE(599119489002373119, 599119491149856767);

┌─────────────────────────────────────────────────┐
│ h3_line(599119489002373119, 599119491149856767) │
├─────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]         │
└─────────────────────────────────────────────────┘
```
