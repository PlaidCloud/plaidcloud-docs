---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART — divide una cadena mediante un delimitador especificado y devuelve la parte indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

Divide una cadena mediante un delimitador especificado y devuelve la parte indicada.

Consulte también: [SPLIT](../split)

## Sintaxis de Analyze

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Ejemplos de Analyze

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

El argumento *position* especifica qué parte se devuelve. Usa un índice basado en 1, pero también acepta valores positivos, negativos o cero:

- Si *position* es un número positivo, devuelve la parte situada en esa posición de izquierda a derecha, o NULL si no existe.
- Si *position* es un número negativo, devuelve la parte situada en esa posición de derecha a izquierda, o NULL si no existe.
- Si *position* es 0, se trata como 1, por lo que devuelve la primera parte de la cadena.

## Tipo de retorno

Cadena. SPLIT_PART devuelve NULL cuando la cadena de entrada, el delimitador o la posición son NULL.

## Ejemplos de SQL

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
