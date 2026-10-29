---
title: "[ NOT ] IN（Lakehouse v1）"
description: "[ NOT ] IN — 値が明示的なリストのいずれかの項目と等しい（または等しくない）場合に true になります。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

値が明示的なリストに含まれる（または含まれない）かどうかを調べます。

## Analyze 構文

```python
table.columns.in_((<value1>, <value2> ...))
```

## Analyze の例

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL 構文

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## SQL の例

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
