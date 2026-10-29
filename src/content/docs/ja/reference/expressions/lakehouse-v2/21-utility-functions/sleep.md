---
title: SLEEP（Lakehouse v2）
description: SLEEP — 指定した秒数だけ実行を一時停止します。成功した場合は 0 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

指定した秒数だけ実行を一時停止します。成功した場合は 0 を返します。

## Analyze 構文

```python
func.sleep(<seconds>)
```

## Analyze の例

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## SQL 構文

```sql
SLEEP(<seconds>)
```

## SQL の例

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
