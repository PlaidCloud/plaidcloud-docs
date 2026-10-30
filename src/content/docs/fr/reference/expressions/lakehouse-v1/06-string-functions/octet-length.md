---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH() est un synonyme de LENGTH().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() est un synonyme de LENGTH().

## Syntaxe Analyze

```python
func.octet_length(<str>)
```

## Exemples Analyze

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## Syntaxe SQL

```sql
OCTET_LENGTH(<str>)
```

## Exemples SQL

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
