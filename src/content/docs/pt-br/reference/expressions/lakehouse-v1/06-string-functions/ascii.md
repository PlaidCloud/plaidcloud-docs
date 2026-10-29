---
title: ASCII (Lakehouse v1)
description: ASCII — retorna o valor numérico do caractere mais à esquerda da string str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

Retorna o valor numérico do caractere mais à esquerda da string str.

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

| Argumentos | Descrição   |
|-----------|-------------|
| `<expr>`  | A string.   |

## Tipo de retorno

`TINYINT`

## Exemplos de SQL

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
