---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — y/x の逆正接を返します。符号を使用して象限を判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

y/x の逆正接を返します。符号を使用して象限を判定します。

## Analyzeの構文

```python
func.atan2(<y>, <x>)
```

## Analyzeの例

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQLの構文

```sql
ATAN2(<y>, <x>)
```

## SQLの例

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
