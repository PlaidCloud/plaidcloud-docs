---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — Joda-Timeの書式パターンを使用して文字列を日時に解析します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Joda-Timeの書式パターンを使用して文字列を日時に解析します。

## Analyzeの構文

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Analyzeの例

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## SQLの例

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
