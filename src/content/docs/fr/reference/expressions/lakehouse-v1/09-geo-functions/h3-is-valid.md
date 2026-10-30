---
title: H3_IS_VALID (Lakehouse v1)
description: H3_IS_VALID — vérifie si l'index H3 donné est valide.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

Vérifie si l'index [H3](https://eng.uber.com/h3/) donné est valide.

## Syntaxe Analyze

```python
func.h3_is_valid(h3)
```

## Exemples Analyze

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_IS_VALID(h3)
```

## Exemples SQL

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
