---
title: SPLIT (Lakehouse v1)
description: SPLIT — 지정한 구분자로 문자열을 분할하고 결과 부분을 배열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split.md
---

지정한 구분자로 문자열을 분할하고 결과 부분을 배열로 반환합니다.

참고: [SPLIT_PART](../split-part)

## Analyze 구문

```python
func.split('<input_string>', '<delimiter>')
```

## Analyze 예제

```python
func.split('PlaidCloud Lakehouse', ' ')
┌─────────────────────────────────────────┐
│ func.split('PlaidCloud Lakehouse', ' ') │
├─────────────────────────────────────────┤
│ ['PlaidCloud Lakehouse']          │
└─────────────────────────────────────────┘
```

## SQL 구문

```sql
SPLIT('<input_string>', '<delimiter>')
```

## 반환 형식

문자열 배열입니다. 입력 문자열 또는 구분자가 NULL이면 SPLIT은 NULL을 반환합니다.

## SQL 예제

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
