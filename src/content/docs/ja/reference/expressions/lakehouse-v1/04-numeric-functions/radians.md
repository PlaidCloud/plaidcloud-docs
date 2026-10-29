---
title: RADIANS（Lakehouse v1）
description: RADIANS — 引数 x を度からラジアンに変換して返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

引数 `x` を度からラジアンに変換して返します。

## Analyze 構文

```python
func.radians( <x> )
```

## Analyze の例

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## SQL 構文

```sql
RADIANS( <x> )
```

## SQL の例

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
