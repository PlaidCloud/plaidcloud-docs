---
title: H3_TO_STRING (Lakehouse v1)
description: H3_TO_STRING — convertit la représentation de l'index H3 donné en sa représentation sous forme de chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

Convertit la représentation de l'index [H3](https://eng.uber.com/h3/) donné en sa représentation sous forme de chaîne.

## Syntaxe Analyze

```python
func.h3_to_string(h3)
```

## Exemples Analyze

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_TO_STRING(h3)
```

## Exemples SQL

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
