---
title: NVL（Lakehouse v1）
description: NVL — <expr1> が NULL の場合は <expr2> を返し、そうでない場合は <expr1> を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nvl.md
---

`<expr1>` が NULL の場合は `<expr2>` を返し、そうでない場合は `<expr1>` を返します。

## Analyze 構文

```python
func.nvl(<expr1>, <expr2>)
```

## Analyze の例

```python
func.nvl(null, 'b'), func.nvl('a', 'b')

┌──────────────────────────────────────────┐
│ func.nvl(null, 'b') │ func.nvl('a', 'b') │
├─────────────────────┼────────────────────┤
│ b                   │ a                  │
└──────────────────────────────────────────┘

func.nvl(null, 2), func.nvl(1, 2)

┌────────────────────────────────────┐
│ func.nvl(null, 2) │ func.nvl(1, 2) │
├───────────────────┼────────────────┤
│                 2 │              1 │
└────────────────────────────────────┘
```

## SQL 構文

```sql
NVL(<expr1>, <expr2>)
```

## エイリアス

- [IFNULL](../ifnull)

## SQL の例

```sql
SELECT NVL(NULL, 'b'), NVL('a', 'b');

┌────────────────────────────────┐
│ nvl(null, 'b') │ nvl('a', 'b') │
├────────────────┼───────────────┤
│ b              │ a             │
└────────────────────────────────┘

SELECT NVL(NULL, 2), NVL(1, 2);

┌──────────────────────────┐
│ nvl(null, 2) │ nvl(1, 2) │
├──────────────┼───────────┤
│            2 │         1 │
└──────────────────────────┘
```
