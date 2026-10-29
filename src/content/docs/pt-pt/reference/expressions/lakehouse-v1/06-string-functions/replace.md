---
title: REPLACE (Lakehouse v1)
description: REPLACE — devolve a cadeia de caracteres str com todas as ocorrências da cadeia from_str substituídas pela cadeia to_str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

Devolve a cadeia de caracteres str com todas as ocorrências da cadeia from_str substituídas pela cadeia to_str.

## Sintaxe do Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Exemplos do Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## Sintaxe SQL

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## Argumentos

| Argumentos   | Descrição                      |
|--------------|--------------------------------|
| `<str>`      | A cadeia de caracteres.        |
| `<from_str>` | A cadeia de origem.            |
| `<to_str>`   | A cadeia de destino.           |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
