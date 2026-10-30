---
title: TO_START_OF_ISO_YEAR（Lakehouse v1）
description: TO_START_OF_ISO_YEAR——返回日期或带时间日期所在 ISO 年的第一天。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-iso-year.md
---

返回日期或带时间的日期（timestamp/datetime）所在 ISO 年的第一天。

## Analyze 语法

```python
func.to_start_of_iso_year(<expr>)
```

## Analyze 示例

```python
func.to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_iso_year('2023-11-12 09:38:18.165575')        │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-02                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_START_OF_ISO_YEAR(<expr>)
```

## 参数

| 参数      | 说明           |
|-----------|----------------|
| `<expr>`  | 日期/时间戳    |

## 返回类型

`DATE`，以“YYYY-MM-DD”格式返回日期。

## SQL 示例

```sql
SELECT
  to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ to_start_of_iso_year('2023-11-12 09:38:18.165575') │
│                        Date                        │
├────────────────────────────────────────────────────┤
│ 2023-01-02                                         │
└────────────────────────────────────────────────────┘
```
