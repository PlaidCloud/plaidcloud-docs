---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — 値をそのまま返します（単項プラス）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

値をそのまま返します（単項プラス）。

## Analyzeの構文

```python
func.positive(<x>)
```

## Analyzeの例

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## SQLの構文

```sql
POSITIVE(<x>)
```

## SQLの例

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
