---
title: ASSUME_NOT_NULL（Lakehouse v1）
description: ASSUME_NOT_NULL — Nullable型の値を、同等のNullableでない値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Nullable型の値を、同等の非 `Nullable` の値に変換します。元の値が `NULL` の場合、結果は不定です。 

## Analyzeの構文

```python
func.assume_not_null(<x>)
```

## Analyzeの例

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

## SQLの構文

```sql
ASSUME_NOT_NULL(<x>)
```

## エイリアス

- [REMOVE_NULLABLE](../remove-nullable)

## 戻り値の型

非 `Nullable` 型の場合は元のデータ型を返し、`Nullable` 型の場合は内包されている非 `Nullable` のデータ型を返します。

## SQLの例

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
