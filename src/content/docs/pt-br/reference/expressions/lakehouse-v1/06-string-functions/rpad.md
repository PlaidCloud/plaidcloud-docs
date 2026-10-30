---
title: RPAD (Lakehouse v1)
description: RPAD — retorna a string str, preenchida à direita com a string padstr até o comprimento de len caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

Retorna a string str, preenchida à direita com a string padstr até o comprimento de len caracteres.
Se str for mais longa que len, o valor retornado é reduzido a len caracteres.

## Sintaxe do Analyze

```python
func.rpad(<str>, <len>, <padstr>)
```

## Exemplos do Analyze

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## Sintaxe SQL

```sql
RPAD(<str>, <len>, <padstr>)
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
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```
