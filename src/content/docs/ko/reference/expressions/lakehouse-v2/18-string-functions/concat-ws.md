---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS — 구분자를 사용하여 문자열을 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

구분자를 사용하여 문자열을 연결합니다.

## Analyze 구문

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Analyze 예제

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL 구문

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## SQL 예제

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
