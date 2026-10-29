---
title: SPLIT (Lakehouse v1)
description: SPLIT – teilt eine Zeichenfolge anhand eines angegebenen Trennzeichens und gibt die resultierenden Teile als Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split.md
---

Teilt eine Zeichenfolge anhand eines angegebenen Trennzeichens und gibt die resultierenden Teile als Array zurück.

Siehe auch: [SPLIT_PART](../split-part)

## Analyze-Syntax

```python
func.split('<input_string>', '<delimiter>')
```

## Analyze-Beispiele

```python
func.split('PlaidCloud Lakehouse', ' ')
┌─────────────────────────────────────────┐
│ func.split('PlaidCloud Lakehouse', ' ') │
├─────────────────────────────────────────┤
│ ['PlaidCloud Lakehouse']          │
└─────────────────────────────────────────┘
```

## SQL-Syntax

```sql
SPLIT('<input_string>', '<delimiter>')
```

## Rückgabetyp

Array von Zeichenfolgen. SPLIT gibt NULL zurück, wenn die Eingabezeichenfolge oder das Trennzeichen NULL ist.

## SQL-Beispiele

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
