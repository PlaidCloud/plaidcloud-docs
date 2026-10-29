---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL — Nullable 유형에 대해 동일한 Nullable이 아닌 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Nullable 유형에 대해 동일한 `Nullable`이 아닌 값을 반환합니다. 원래 값이 `NULL`인 경우 결과는 정해지지 않습니다. 

## Analyze 구문

```python
func.assume_not_null(<x>)
```

## Analyze 예제

```python
With a table like:

┌────────────────────┐
│        x  │   y    │
├────────────────────┤
│         1 │   NULL │
│         2 │      3 │
└────────────────────┘

func.assume_not_null(y)
┌─────────────────────────┐
│ func.assume_not_null(y) │
├─────────────────────────┤
│                       0 │
│                       3 │
└─────────────────────────┘
```

## SQL 구문

```sql
ASSUME_NOT_NULL(<x>)
```

## 별칭

- [REMOVE_NULLABLE](../remove-nullable)

## 반환 유형

`Nullable`이 아닌 유형에서는 원래 데이터 유형을 반환하고, `Nullable` 유형에서는 내장된 `Nullable`이 아닌 데이터 유형을 반환합니다.

## SQL 예제

```sql
CREATE TABLE default.t_null ( x int,  y int null);

INSERT INTO default.t_null values (1, null), (2, 3);

SELECT ASSUME_NOT_NULL(y), REMOVE_NULLABLE(y) FROM t_null;

┌─────────────────────────────────────────┐
│ assume_not_null(y) │ remove_nullable(y) │
├────────────────────┼────────────────────┤
│                  0 │                  0 │
│                  3 │                  3 │
└─────────────────────────────────────────┘
```
