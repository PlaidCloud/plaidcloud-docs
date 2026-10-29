---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH — OCTET_LENGTH() é um sinônimo de LENGTH().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() é um sinônimo de LENGTH().

## Sintaxe do Analyze

```python
func.octet_length(<str>)
```

## Exemplos do Analyze

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## Sintaxe SQL

```sql
OCTET_LENGTH(<str>)
```

## Exemplos de SQL

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
