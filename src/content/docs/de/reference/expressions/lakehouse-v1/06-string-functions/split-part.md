---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART – teilt eine Zeichenfolge anhand eines angegebenen Trennzeichens und gibt den angegebenen Teil zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

Teilt eine Zeichenfolge anhand eines angegebenen Trennzeichens und gibt den angegebenen Teil zurück.

Siehe auch: [SPLIT](../split)

## Analyze-Syntax

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Analyze-Beispiele

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

Das Argument *position* gibt an, welcher Teil zurückgegeben wird. Es verwendet einen bei 1 beginnenden Index, akzeptiert aber auch positive, negative oder null als Wert:

- Ist *position* eine positive Zahl, wird der Teil an dieser Position von links nach rechts zurückgegeben, oder NULL, wenn er nicht existiert.
- Ist *position* eine negative Zahl, wird der Teil an dieser Position von rechts nach links zurückgegeben, oder NULL, wenn er nicht existiert.
- Ist *position* 0, wird sie wie 1 behandelt, sodass der erste Teil der Zeichenfolge zurückgegeben wird.

## Rückgabetyp

Zeichenfolge. SPLIT_PART gibt NULL zurück, wenn die Eingabezeichenfolge, das Trennzeichen oder die Position NULL ist.

## SQL-Beispiele

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
