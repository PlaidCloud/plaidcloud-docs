---
title: LPAD (Lakehouse v1)
description: LPAD — retorna a string str, preenchida à esquerda com a string padstr até o comprimento de len caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

Retorna a string str, preenchida à esquerda com a string padstr até o comprimento de len caracteres.
Se str for mais longa que len, o valor retornado é reduzido a len caracteres.

## Sintaxe do Analyze

```python
func.lpad(<str>, <len>, <padstr>)
```

## Exemplos do Analyze

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## Sintaxe SQL

```sql
LPAD(<str>, <len>, <padstr>)
```

## Argumentos

| Argumentos | Descrição                    |
|------------|------------------------------|
| `<str>`    | A string.                    |
| `<len>`    | O comprimento.               |
| `<padstr>` | A string de preenchimento.   |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

```sql
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```
