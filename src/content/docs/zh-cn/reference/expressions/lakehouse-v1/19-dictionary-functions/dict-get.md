---
title: DICT_GET (Lakehouse v1)
description: DICT_GET：使用提供的键表达式从字典中检索指定属性的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

使用提供的键表达式从字典中检索指定属性的值。

## SQL 语法

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| 参数 | 说明 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | 字典的名称。 |
| attr_name | 要检索其值的字典属性的名称。 |
| key_expr | 用于定位字典中特定条目的键表达式。它表示字典主键的值，用于检索对应的数据。 |

## SQL 示例
