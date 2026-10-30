---
title: CHAR (Lakehouse v2)
description: CHAR — 지정한 ASCII 코드에 해당하는 문자를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

지정한 ASCII 코드에 해당하는 문자를 반환합니다.

## Analyze 구문

```python
func.char(<code>)
```

## Analyze 예제

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## SQL 구문

```sql
CHAR(<code>)
```

## SQL 예제

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
