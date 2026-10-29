---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART — 指定した区切り文字で文字列を分割し、指定した部分を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

指定した区切り文字で文字列を分割し、指定した部分を返します。

関連項目: [SPLIT](../split)

## Analyze の構文

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Analyze の例

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## SQL構文

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

*position* 引数は、返す部分を指定します。1から始まるインデックスを使用しますが、正の値、負の値、ゼロも指定できます。

- *position* が正の数の場合は、左から右に数えた位置の部分を返します。その位置に部分が存在しない場合は NULL を返します。
- *position* が負の数の場合は、右から左に数えた位置の部分を返します。その位置に部分が存在しない場合は NULL を返します。
- *position* が 0 の場合は 1 として扱われ、文字列の最初の部分を返します。

## 戻り値の型

文字列。入力文字列、区切り文字、位置のいずれかが NULL の場合、SPLIT_PART は NULL を返します。

## SQLの例

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
