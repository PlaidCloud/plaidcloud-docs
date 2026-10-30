---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT — 숫자를 쉼표와 소수점 이하 두 자리가 있는 통화 문자열로 서식 지정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

숫자를 쉼표와 소수점 이하 두 자리가 있는 통화 문자열로 서식 지정합니다.

## Analyze 구문

```python
func.money_format(<num>)
```

## Analyze 예제

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## SQL 구문

```sql
MONEY_FORMAT(<num>)
```

## SQL 예제

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
