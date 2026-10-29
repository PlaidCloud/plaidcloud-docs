---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY — 지정한 바이너리 형식에 따라 VARCHAR 문자열을 바이너리 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

지정한 바이너리 형식에 따라 VARCHAR 문자열을 바이너리 값으로 변환합니다.

## Analyze 구문

```python
func.to_binary(<str>, <format>)
```

## Analyze 예제

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 구문

```sql
TO_BINARY(<str>, <format>)
```

## SQL 예제

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
