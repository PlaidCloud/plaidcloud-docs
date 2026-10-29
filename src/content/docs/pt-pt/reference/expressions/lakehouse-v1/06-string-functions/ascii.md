---
title: ASCII (Lakehouse v1)
description: ASCII — devolve o valor numérico do caráter mais à esquerda da cadeia de caracteres str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

Devolve o valor numérico do caráter mais à esquerda da cadeia de caracteres str.

## Sintaxe do Analyze

```python
func.ascii(<expr>)
```

## Exemplos do Analyze

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## Sintaxe SQL

```sql
ASCII(<expr>)
```

## Argumentos

| Argumentos | Descrição                 |
|-----------|---------------------------|
| `<expr>`  | A cadeia de caracteres.   |

## Tipo de Retorno

`TINYINT`

## Exemplos SQL

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
