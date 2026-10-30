---
title: H3_GET_RESOLUTION (Lakehouse v1)
description: H3_GET_RESOLUTION — renvoie la résolution de l'index H3 donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-resolution.md
---

Renvoie la résolution de l'index [H3](https://eng.uber.com/h3/) donné.

## Syntaxe Analyze

```python
func.h3_get_resolution(h3)
```

## Exemples Analyze

```python
func.h3_get_resolution(644325524701193974)

┌────────────────────────────────────────────┐
│ func.h3_get_resolution(644325524701193974) │
├────────────────────────────────────────────┤
│                                         15 │
└────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_GET_RESOLUTION(h3)
```

## Exemples SQL

```sql
SELECT H3_GET_RESOLUTION(644325524701193974);

┌───────────────────────────────────────┐
│ h3_get_resolution(644325524701193974) │
├───────────────────────────────────────┤
│                                    15 │
└───────────────────────────────────────┘
```
