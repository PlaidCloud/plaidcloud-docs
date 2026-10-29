---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY — 지정한 바이너리 형식에 따라 바이너리 값을 VARCHAR 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

지정한 바이너리 형식에 따라 바이너리 값을 VARCHAR 문자열로 변환합니다.

## Analyze 구문

```python
func.from_binary(<binary>, <format>)
```

## Analyze 예제

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 구문

```sql
FROM_BINARY(<binary>, <format>)
```

## SQL 예제

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
