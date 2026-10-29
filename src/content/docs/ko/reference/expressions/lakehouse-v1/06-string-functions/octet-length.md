---
title: OCTET_LENGTH (Lakehouse v1)
description: OCTET_LENGTH — OCTET_LENGTH()는 LENGTH()의 동의어입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH()는 LENGTH()의 동의어입니다.

## Analyze 구문

```python
func.octet_length(<str>)
```

## Analyze 예제

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## SQL 구문

```sql
OCTET_LENGTH(<str>)
```

## SQL 예제

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
