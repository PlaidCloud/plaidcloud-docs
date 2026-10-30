---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE：将值转换为其可为空的等效值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

将值转换为其可为空的等效值。

对某个值应用此函数时，它会检查该值是否已能够容纳 NULL 值。如果该值已能容纳 NULL 值，函数将原样返回该值，不作任何更改。

但是，如果该值不能容纳 NULL 值，TO_NULLABLE 函数会修改该值，使其能够容纳 NULL 值。具体做法是将该值包装在可容纳 NULL 值的结构中，这意味着该值今后可以容纳 NULL 值。

## Analyze 语法

```python
func.to_nullable(x);
```

## Analyze 示例

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## SQL 语法

```sql
TO_NULLABLE(x);
```

## 参数

| 参数 | 说明 |
|-----------|----------------------------|
| x | 原始值。 |


## 返回类型

返回与输入值数据类型相同的值；如果输入值尚不可为空，则将其包装在可为空的容器中。

## SQL 示例

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
