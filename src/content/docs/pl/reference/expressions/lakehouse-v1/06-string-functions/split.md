---
title: SPLIT (Lakehouse v1)
description: SPLIT — dzieli ciąg znaków za pomocą podanego ogranicznika i zwraca otrzymane części jako tablicę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split.md
---

Dzieli ciąg znaków za pomocą podanego ogranicznika i zwraca otrzymane części jako tablicę.

Zobacz także: [SPLIT_PART](../split-part)

## Składnia Analyze

```python
func.split('<input_string>', '<delimiter>')
```

## Przykłady Analyze

```python
func.split('PlaidCloud Lakehouse', ' ')
┌─────────────────────────────────────────┐
│ func.split('PlaidCloud Lakehouse', ' ') │
├─────────────────────────────────────────┤
│ ['PlaidCloud Lakehouse']          │
└─────────────────────────────────────────┘
```

## Składnia SQL

```sql
SPLIT('<input_string>', '<delimiter>')
```

## Typ zwracany

Tablica ciągów znaków. SPLIT zwraca NULL, gdy ciąg wejściowy lub ogranicznik ma wartość NULL.

## Przykłady SQL

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
