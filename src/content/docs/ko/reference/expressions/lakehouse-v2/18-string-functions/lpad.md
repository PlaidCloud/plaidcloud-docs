---
title: LPAD (Lakehouse v2)
description: LPAD — 문자열의 왼쪽을 채움 문자열로 채워 지정한 길이로 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

문자열의 왼쪽을 채움 문자열로 채워 지정한 길이로 만듭니다.

## Analyze 구문

```python
func.lpad(<str>, <len>, <pad>)
```

## Analyze 예제

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## SQL 구문

```sql
LPAD(<str>, <len>, <pad>)
```

## SQL 예제

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
