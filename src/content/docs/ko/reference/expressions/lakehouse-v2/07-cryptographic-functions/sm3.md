---
title: SM3 (Lakehouse v2)
description: SM3 — 문자열의 SM3 해시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

문자열의 SM3 해시를 반환합니다.

## Analyze 구문

```python
func.sm3(<str>)
```

## Analyze 예제

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## SQL 구문

```sql
SM3(<str>)
```

## SQL 예제

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
