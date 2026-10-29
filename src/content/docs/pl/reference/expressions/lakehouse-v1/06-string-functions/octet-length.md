---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH — OCTET_LENGTH() jest synonimem funkcji LENGTH().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() jest synonimem funkcji LENGTH().

## Składnia Analyze

```python
func.octet_length(<str>)
```

## Przykłady Analyze

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## Składnia SQL

```sql
OCTET_LENGTH(<str>)
```

## Przykłady SQL

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
