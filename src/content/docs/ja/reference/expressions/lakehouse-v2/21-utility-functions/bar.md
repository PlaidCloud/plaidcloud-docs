---
title: BAR（Lakehouse v2）
description: "PlaidCloud Lakehouse で BAR ユーティリティ関数を使用します。範囲内の値を視覚的なバー文字列で表現して返します。テキストベースの可視化に便利です。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

範囲内の値を視覚的なバー文字列で表現して返します。テキストベースの可視化に便利です。

## Analyze 構文

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Analyze の例

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## SQL 構文

```sql
BAR(<value>, <min>, <max>, <width>)
```

## SQL の例

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
