---
title: CEIL（Lakehouse v1）
description: CEIL——将数字向上取整。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

将数字向上取整。

## Analyze 语法

```python
func.ceil( <x> )
```

## Analyze 示例

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## SQL 语法

```sql
CEIL( <x> )
```

## 别名

- [CEILING](../ceiling)

## SQL 示例

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
