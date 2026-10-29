---
title: INSTR (Lakehouse v2)
description: INSTR — 문자열에서 부분 문자열이 처음 나타나는 위치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

문자열에서 부분 문자열이 처음 나타나는 위치를 반환합니다.

## Analyze 구문

```python
func.instr(<str>, <substr>)
```

## Analyze 예제

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL 구문

```sql
INSTR(<str>, <substr>)
```

## SQL 예제

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
