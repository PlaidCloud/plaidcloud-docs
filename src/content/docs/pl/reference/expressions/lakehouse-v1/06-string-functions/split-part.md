---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART — dzieli ciąg znaków za pomocą podanego ogranicznika i zwraca wskazaną część.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

Dzieli ciąg znaków za pomocą podanego ogranicznika i zwraca wskazaną część.

Zobacz także: [SPLIT](../split)

## Składnia Analyze

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Przykłady Analyze

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

Argument *position* określa, którą część zwrócić. Używa indeksu liczonego od 1, ale może też przyjmować wartości dodatnie, ujemne lub zero:

- Jeśli *position* jest liczbą dodatnią, funkcja zwraca część na tej pozycji licząc od lewej do prawej lub NULL, jeśli taka część nie istnieje.
- Jeśli *position* jest liczbą ujemną, funkcja zwraca część na tej pozycji licząc od prawej do lewej lub NULL, jeśli taka część nie istnieje.
- Jeśli *position* wynosi 0, jest traktowane jak 1, co w praktyce zwraca pierwszą część ciągu.

## Typ zwracany

Ciąg znaków. SPLIT_PART zwraca NULL, gdy ciąg wejściowy, ogranicznik lub pozycja ma wartość NULL.

## Przykłady SQL

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
