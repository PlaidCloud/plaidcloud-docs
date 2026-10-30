---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64 — 64비트 SipHash 해시 값을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

64비트 [SipHash](https://en.wikipedia.org/wiki/SipHash) 해시 값을 생성합니다.

## Analyze 구문

```python
func.siphash64(<expr>)
```

## Analyze 예제

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## SQL 구문

```sql
SIPHASH64(<expr>)
```

## 별칭

- [SIPHASH](../siphash)

## SQL 예제

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
