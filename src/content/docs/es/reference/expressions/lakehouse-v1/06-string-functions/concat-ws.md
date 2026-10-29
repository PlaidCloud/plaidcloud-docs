---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS — CONCAT_WS() significa concatenar con separador y es una forma especial de CONCAT().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() significa «Concatenate With Separator» (concatenar con separador) y es una forma especial de CONCAT(). El primer argumento es el separador del resto de los argumentos. El separador se agrega entre las cadenas que se van a concatenar. El separador puede ser una cadena, al igual que el resto de los argumentos. Si el separador es NULL, el resultado es NULL.

CONCAT_WS() no omite las cadenas vacías. Sin embargo, sí omite cualquier valor NULL que aparezca después del argumento separador.

## Sintaxis de Analyze

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Ejemplos de Analyze

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## Argumentos

| Argumentos     | Descripción   |
|---------------| ------------- |
| `<separator>` | columna de cadena |
| `<expr1>`     | columna de valores  |

## Tipo de retorno

Un valor de tipo de datos `VARCHAR` o de tipo de datos `NULL`.

## Ejemplos de SQL

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
