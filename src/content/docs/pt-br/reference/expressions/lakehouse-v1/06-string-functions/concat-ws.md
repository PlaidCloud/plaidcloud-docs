---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS — CONCAT_WS() significa Concatenate With Separator (concatenar com separador) e é uma forma especial de CONCAT().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() significa Concatenate With Separator (concatenar com separador) e é uma forma especial de CONCAT(). O primeiro argumento é o separador dos demais argumentos. O separador é adicionado entre as strings a serem concatenadas. O separador pode ser uma string, assim como os demais argumentos. Se o separador for NULL, o resultado será NULL.

CONCAT_WS() não ignora strings vazias. No entanto, ignora quaisquer valores NULL após o argumento separador.

## Sintaxe do Analyze

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Exemplos do Analyze

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## Argumentos

| Argumentos    | Descrição         |
|---------------| ----------------- |
| `<separator>` | coluna de string  |
| `<expr1>`     | coluna de valor   |

## Tipo de retorno

Um valor do tipo de dados `VARCHAR` ou `NULL`.

## Exemplos de SQL

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
