---
title: SLEEP (Lakehouse v2)
description: SLEEP：将执行暂停指定的秒数。成功时返回 0。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

将执行暂停指定的秒数。成功时返回 0。

## Analyze 语法

```python
func.sleep(<seconds>)
```

## Analyze 示例

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## SQL 语法

```sql
SLEEP(<seconds>)
```

## SQL 示例

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
