---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART — 지정한 구분자로 문자열을 분할하고 지정한 부분을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

지정한 구분자로 문자열을 분할하고 지정한 부분을 반환합니다.

참고: [SPLIT](../split)

## Analyze 구문

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Analyze 예제

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## SQL 구문

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

*position* 인수는 반환할 부분을 지정합니다. 1부터 시작하는 인덱스를 사용하지만 양수, 음수, 0도 받을 수 있습니다.

- *position*이 양수이면 왼쪽에서 오른쪽으로 해당 위치의 부분을 반환하며, 없으면 NULL을 반환합니다.
- *position*이 음수이면 오른쪽에서 왼쪽으로 해당 위치의 부분을 반환하며, 없으면 NULL을 반환합니다.
- *position*이 0이면 1로 처리되어 사실상 문자열의 첫 번째 부분을 반환합니다.

## 반환 형식

문자열입니다. 입력 문자열, 구분자 또는 위치 중 하나라도 NULL이면 SPLIT_PART는 NULL을 반환합니다.

## SQL 예제

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
