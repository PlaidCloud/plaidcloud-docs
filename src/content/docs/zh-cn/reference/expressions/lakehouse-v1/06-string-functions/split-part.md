---
title: SPLIT_PART（Lakehouse v1）
description: SPLIT_PART——使用指定分隔符拆分字符串并返回指定的部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

使用指定分隔符拆分字符串并返回指定的部分。

另请参阅：[SPLIT](../split)

## Analyze 语法

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Analyze 示例

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## SQL 语法

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

*position* 参数指定要返回哪一部分。它使用从 1 开始的索引，但也可以接受正数、负数或零：

- 如果 *position* 为正数，则从左到右返回该位置的部分；该部分不存在时返回 NULL。
- 如果 *position* 为负数，则从右到左返回该位置的部分；该部分不存在时返回 NULL。
- 如果 *position* 为 0，则按 1 处理，即返回字符串的第一部分。

## 返回类型

字符串。当输入字符串、分隔符或位置为 NULL 时，SPLIT_PART 返回 NULL。

## SQL 示例

```sql
-- Use a space as the delimiter
-- SPLIT_PART returns a specific part.
SELECT SPLIT_PART('PlaidCloud Lakehouse', ' ', 1);

split_part('PlaidCloud Lakehouse', ' ', 1)|
------------------------------------------+
PlaidCloud Lakehouse                      |

-- Use an empty string as the delimiter or a delimiter that does not exist in the input string
-- SPLIT_PART returns the entire input string.
SELECT SPLIT_PART('PlaidCloud Lakehouse', '', 1);

split_part('PlaidCloud Lakehouse', '', 1)|
-----------------------------------+
PlaidCloud Lakehouse                     |

SELECT SPLIT_PART('PlaidCloud Lakehouse', ',', 1);

split_part('PlaidCloud Lakehouse', ',', 1)|
------------------------------------+
PlaidCloud Lakehouse                      |

-- Use '    ' (tab) as the delimiter
-- SPLIT_PART returns individual fields.
SELECT SPLIT_PART('2023-10-19 15:30:45   INFO   Log message goes here', '   ', 3);

split_part('2023-10-19 15:30:45   info   log message goes here', '   ', 3)|
--------------------------------------------------------------------------+
Log message goes here                                                     |

-- SPLIT_PART returns an empty string as the specified part does not exist at all.
SELECT SPLIT_PART('2023-10-19 15:30:45   INFO   Log message goes here', '   ', 4);

split_part('2023-10-19 15:30:45   info   log message goes here', '   ', 4)|
--------------------------------------------------------------------------+
                                                                          |
```
