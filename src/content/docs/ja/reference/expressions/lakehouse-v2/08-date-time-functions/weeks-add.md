---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — 日付に指定した週数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

日付に指定した週数を加算します。

## Analyzeの構文

```python
func.weeks_add(<date>, <n>)
```

## Analyzeの例

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQLの構文

```sql
WEEKS_ADD(<date>, <n>)
```

## SQLの例

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
