---
title: SPLIT (Lakehouse v1)
description: SPLIT — 指定した区切り文字で文字列を分割し、分割結果を配列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split.md
---

指定した区切り文字で文字列を分割し、分割結果を配列として返します。

関連項目: [SPLIT_PART](../split-part)

## Analyze の構文

```python
func.split('<input_string>', '<delimiter>')
```

## Analyze の例

```python
func.split('PlaidCloud Lakehouse', ' ')
┌─────────────────────────────────────────┐
│ func.split('PlaidCloud Lakehouse', ' ') │
├─────────────────────────────────────────┤
│ ['PlaidCloud Lakehouse']          │
└─────────────────────────────────────────┘
```

## SQL構文

```sql
SPLIT('<input_string>', '<delimiter>')
```

## 戻り値の型

文字列の配列。入力文字列または区切り文字のいずれかが NULL の場合、SPLIT は NULL を返します。

## SQLの例

```sql
-- Use a space as the delimiter
-- SPLIT returns an array with two parts.
SELECT SPLIT('PlaidCloud Lakehouse', ' ');

split('PlaidCloud Lakehouse', ' ')|
----------------------------------+
['PlaidCloud','Lakehouse']        |

-- Use an empty string as the delimiter or a delimiter that does not exist in the input string
-- SPLIT returns an array containing the entire input string as a single part.
SELECT SPLIT('PlaidCloud Lakehouse', '');

split('databend cloud', '')|
----------------------------------+
['PlaidCloud Lakehouse']    |

SELECT SPLIT('PlaidCloud Lakehouse', ',');

split('databend cloud', ',')|
----------------------------------+
['PlaidCloud Lakehouse']    |

-- Use '	' (tab) as the delimiter
-- SPLIT returns an array with timestamp, log level, and message.

SELECT SPLIT('2023-10-19 15:30:45	INFO	Log message goes here', '	');

split('2023-10-19 15:30:45\tinfo\tlog message goes here', '\t')|
---------------------------------------------------------------+
['2023-10-19 15:30:45','INFO','Log message goes here']         |
```
