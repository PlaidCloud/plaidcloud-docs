---
title: RAND()（Lakehouse v1）
description: RAND() — 0 <= v < 1 の範囲のランダムな浮動小数点値 v を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

0 &lt;= v &lt; 1.0 の範囲のランダムな浮動小数点値 v を返します。i &lt;= R &lt; j の範囲のランダムな整数 R を取得するには、式 FLOOR(i + RAND() * (j − i)) を使用します。

## Analyze 構文

```python
func.rand()
```

## Analyze の例

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## SQL 構文

```sql
RAND()
```

## SQL の例

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
