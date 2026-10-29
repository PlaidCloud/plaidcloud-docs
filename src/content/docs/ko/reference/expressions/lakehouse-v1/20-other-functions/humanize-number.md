---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER — 읽기 쉬운 숫자를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

읽기 쉬운 숫자를 반환합니다.

## Analyze 구문

```python
func.humanize_number(x);
```

## Analyze 예제

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## SQL 구문

```sql
HUMANIZE_NUMBER(x);
```

## 인수

| 인수 | 설명 |
|-----------|----------------------------|
| x         | 숫자 크기입니다.        |


## 반환 유형

문자열.

## SQL 예제

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
