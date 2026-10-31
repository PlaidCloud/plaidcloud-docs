---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH — OCTET_LENGTH() は LENGTH() の同義語です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() は LENGTH() の同義語です。

## Analyze の構文

```python
func.octet_length(<str>)
```

## Analyze の例

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## SQL構文

```sql
OCTET_LENGTH(<str>)
```

## SQLの例

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
