---
title: REPEAT (Lakehouse v1)
description: REPEAT — 文字列 str を count 回繰り返した文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

文字列 str を count 回繰り返した文字列を返します。count が 1 未満の場合は空文字列を返します。str または count が NULL の場合は NULL を返します。

## Analyze の構文

```python
func.repeat(<str>, <count>)
```

## Analyze の例

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## SQL構文

```sql
REPEAT(<str>, <count>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<str>`   | 文字列。 |
| `<count>` | 回数。 |

## SQLの例

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
