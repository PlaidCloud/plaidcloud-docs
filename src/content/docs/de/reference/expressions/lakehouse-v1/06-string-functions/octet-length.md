---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH – OCTET_LENGTH() ist ein Synonym für LENGTH().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() ist ein Synonym für LENGTH().

## Analyze-Syntax

```python
func.octet_length(<str>)
```

## Analyze-Beispiele

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## SQL-Syntax

```sql
OCTET_LENGTH(<str>)
```

## SQL-Beispiele

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
