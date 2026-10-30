---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE — 年と年内の通算日から日付を作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

年と年内の通算日から日付を作成します。

## Analyzeの構文

```python
func.makedate(<year>, <dayofyear>)
```

## Analyzeの例

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## SQLの構文

```sql
MAKEDATE(<year>, <dayofyear>)
```

## SQLの例

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
