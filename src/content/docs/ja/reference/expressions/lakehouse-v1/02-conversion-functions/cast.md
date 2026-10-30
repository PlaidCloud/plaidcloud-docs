---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: — 値を1つのデータ型から別のデータ型に変換します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

値を1つのデータ型から別のデータ型に変換します。`::`はCASTのエイリアスです。

関連項目：[TRY_CAST](../try-cast)

## Analyzeの構文

```python
func.cast( <expr>, <data_type> )
```

## Analyzeの例

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## SQLの構文

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## SQLの例

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
