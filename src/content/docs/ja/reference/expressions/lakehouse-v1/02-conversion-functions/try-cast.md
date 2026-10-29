---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST — 値を1つのデータ型から別のデータ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

値を1つのデータ型から別のデータ型に変換します。エラーが発生した場合はNULLを返します。

関連項目：[CAST](../cast)

## Analyzeの構文

```python
func.try_cast( <expr>, <data_type> )
```

## Analyzeの例

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## SQLの構文

```sql
TRY_CAST( <expr> AS <data_type> )
```

## SQLの例

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
