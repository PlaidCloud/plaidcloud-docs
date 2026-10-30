---
title: LPAD (Lakehouse v1)
description: LPAD — devolve a cadeia de caracteres str, preenchida à esquerda com a cadeia padstr até ao comprimento de len caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

Devolve a cadeia de caracteres str, preenchida à esquerda com a cadeia padstr até ao comprimento de len caracteres.
Se str for mais longa do que len, o valor devolvido é encurtado para len caracteres.

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

| Argumentos | Descrição                         |
|------------|-----------------------------------|
| `<str>`    | A cadeia de caracteres.           |
| `<len>`    | O comprimento.                    |
| `<padstr>` | A cadeia de preenchimento.        |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

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
