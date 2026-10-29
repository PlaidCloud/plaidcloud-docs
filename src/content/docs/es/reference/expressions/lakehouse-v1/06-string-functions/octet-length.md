---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH — OCTET_LENGTH() es un sinónimo de LENGTH().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() es un sinónimo de LENGTH().

## Sintaxis de Analyze

```python
func.octet_length(<str>)
```

## Ejemplos de Analyze

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## Sintaxis SQL

```sql
OCTET_LENGTH(<str>)
```

## Ejemplos de SQL

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
