---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART — divide uma string usando um delimitador especificado e retorna a parte indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

Divide uma string usando um delimitador especificado e retorna a parte indicada.

Veja também: [SPLIT](../split)

## Sintaxe do Analyze

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Exemplos do Analyze

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

O argumento *position* especifica qual parte retornar. Ele usa um índice baseado em 1, mas também aceita valores positivos, negativos ou zero:

- Se *position* for um número positivo, retorna a parte nessa posição da esquerda para a direita, ou NULL se ela não existir.
- Se *position* for um número negativo, retorna a parte nessa posição da direita para a esquerda, ou NULL se ela não existir.
- Se *position* for 0, é tratado como 1, retornando na prática a primeira parte da string.

## Tipo de retorno

String. SPLIT_PART retorna NULL quando a string de entrada, o delimitador ou a posição é NULL.

## Exemplos de SQL

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
