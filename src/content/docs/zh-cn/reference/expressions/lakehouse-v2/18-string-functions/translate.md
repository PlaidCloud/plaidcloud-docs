---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE：根据字符映射替换字符串中的字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

根据字符映射替换字符串中的字符。

## Analyze 语法

```python
func.translate(<str>, <from>, <to>)
```

## Analyze 示例

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## SQL 语法

```sql
TRANSLATE(<str>, <from>, <to>)
```

## SQL 示例

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
