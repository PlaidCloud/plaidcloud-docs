---
title: SPLIT (Lakehouse v1)
description: SPLIT — divide uma cadeia de caracteres através de um delimitador especificado e devolve as partes resultantes como uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split.md
---

Divide uma cadeia de caracteres através de um delimitador especificado e devolve as partes resultantes como uma matriz.

Veja também: [SPLIT_PART](../split-part)

## Sintaxe do Analyze

```python
func.split('<input_string>', '<delimiter>')
```

## Exemplos do Analyze

```python
func.split('PlaidCloud Lakehouse', ' ')
┌─────────────────────────────────────────┐
│ func.split('PlaidCloud Lakehouse', ' ') │
├─────────────────────────────────────────┤
│ ['PlaidCloud Lakehouse']          │
└─────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
SPLIT('<input_string>', '<delimiter>')
```

## Tipo de Retorno

Matriz de cadeias de caracteres. SPLIT devolve NULL quando a cadeia de entrada ou o delimitador for NULL.

## Exemplos SQL

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
