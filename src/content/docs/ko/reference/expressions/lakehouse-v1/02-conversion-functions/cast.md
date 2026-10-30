---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: — 값을 한 데이터 형식에서 다른 데이터 형식으로 변환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

값을 한 데이터 형식에서 다른 데이터 형식으로 변환합니다. `::`는 CAST의 별칭입니다.

참고: [TRY_CAST](../try-cast)

## Analyze 구문

```python
func.cast( <expr>, <data_type> )
```

## Analyze 예제

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## SQL 구문

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## SQL 예제

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
