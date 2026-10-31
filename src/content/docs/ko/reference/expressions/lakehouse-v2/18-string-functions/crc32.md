---
title: CRC32 (Lakehouse v2)
description: CRC32 — 문자열의 CRC-32 체크섬을 부호 없는 정수로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

문자열의 CRC-32 체크섬을 부호 없는 정수로 반환합니다.

## Analyze 구문

```python
func.crc32(<str>)
```

## Analyze 예제

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## SQL 구문

```sql
CRC32(<str>)
```

## SQL 예제

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
