---
title: INSTR (Lakehouse v1)
description: INSTR — devuelve la posición de la primera aparición de la subcadena substr en la cadena str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

Devuelve la posición de la primera aparición de la subcadena substr en la cadena str.
Es igual que la forma de dos argumentos de LOCATE(), salvo que el orden de los argumentos está invertido.

## Sintaxis de Analyze

```python
func.instr(<str>, <substr>)
```

## Ejemplos de Analyze

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## Sintaxis SQL

```sql
INSTR(<str>, <substr>)
```

## Argumentos

| Argumentos  | Descripción    |
|------------|----------------|
| `<str>`    | La cadena.    |
| `<substr>` | La subcadena. |

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
