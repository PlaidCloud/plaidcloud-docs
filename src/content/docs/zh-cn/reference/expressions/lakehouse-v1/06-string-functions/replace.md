---
title: REPLACE（Lakehouse v1）
description: REPLACE——返回将字符串 str 中所有出现的字符串 from_str 替换为字符串 to_str 后的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

返回将字符串 str 中所有出现的字符串 from_str 替换为字符串 to_str 后的字符串。

## Analyze 语法

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Analyze 示例

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## SQL 语法

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## 参数

| 参数    | 说明      |
|--------------|------------------|
| `<str>`      | 字符串。      |
| `<from_str>` | 源字符串。 |
| `<to_str>`   | 目标字符串。   |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
