---
title: RPAD (Lakehouse v1)
description: RPAD — devolve a cadeia de caracteres str, preenchida à direita com a cadeia padstr até ao comprimento de len caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

Devolve a cadeia de caracteres str, preenchida à direita com a cadeia padstr até ao comprimento de len caracteres.
Se str for mais longa do que len, o valor devolvido é encurtado para len caracteres.

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

| Argumentos | Descrição                  |
|------------|----------------------------|
| `<str>`    | A cadeia de caracteres.    |
| `<len>`    | O comprimento.             |
| `<padstr>` | A cadeia de preenchimento. |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

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
