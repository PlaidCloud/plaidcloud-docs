---
title: CRC32 (Lakehouse v1)
description: CRC32 — x의 CRC32 체크섬을 반환합니다. 'x'는 문자열이어야 하며, 가능한 경우 문자열이 아니어도 문자열로 처리됩니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

`x`의 CRC32 체크섬을 반환합니다. 'x'는 문자열이어야 하며, 문자열이 아니더라도 가능하면 문자열로 처리됩니다.

## Analyze 구문

```python
func.crc32( '<x>' )
```

## Analyze 예시

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## SQL 구문

```sql
CRC32( '<x>' )
```

## SQL 예시

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
