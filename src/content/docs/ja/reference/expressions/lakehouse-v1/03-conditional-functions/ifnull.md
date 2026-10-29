---
title: IFNULL（Lakehouse v1）
description: IFNULL — <expr1> が NULL の場合は <expr2> を返し、そうでない場合は <expr1> を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/ifnull.md
---

`<expr1>` が NULL の場合は `<expr2>` を返し、そうでない場合は `<expr1>` を返します。

## Analyze 構文

```python
func.ifnull(<expr1>, <expr2>)
```

## Analyze の例

```python
func.ifnull(null, 'b'), func.ifnull('a', 'b')

┌────────────────────────────────────────────────┐
│ func.ifnull(null, 'b') │ func.ifnull('a', 'b') │
├────────────────────────┼───────────────────────┤
│ b                      │ a                     │
└────────────────────────────────────────────────┘

func.ifnull(null, 2), func.ifnull(1, 2)

┌──────────────────────────────────────────┐
│ func.ifnull(null, 2) │ func.ifnull(1, 2) │
├──────────────────────┼───────────────────┤
│                    2 │                 1 │
└──────────────────────────────────────────┘
```

## SQL 構文

```sql
IFNULL(<expr1>, <expr2>)
```

## エイリアス

- [NVL](../nvl)

## SQL の例

```sql
SELECT IFNULL(NULL, 'b'), IFNULL('a', 'b');

┌──────────────────────────────────────┐
│ ifnull(null, 'b') │ ifnull('a', 'b') │
├───────────────────┼──────────────────┤
│ b                 │ a                │
└──────────────────────────────────────┘

SELECT IFNULL(NULL, 2), IFNULL(1, 2);

┌────────────────────────────────┐
│ ifnull(null, 2) │ ifnull(1, 2) │
├─────────────────┼──────────────┤
│               2 │            1 │
└────────────────────────────────┘
```
