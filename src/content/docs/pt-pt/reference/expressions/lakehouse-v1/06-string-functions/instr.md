---
title: INSTR (Lakehouse v1)
description: INSTR — devolve a posição da primeira ocorrência da subcadeia substr na cadeia de caracteres str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

Devolve a posição da primeira ocorrência da subcadeia substr na cadeia de caracteres str.
É equivalente à forma de dois argumentos de LOCATE(), exceto que a ordem dos argumentos está invertida.

## Sintaxe do Analyze

```python
func.instr(<str>, <substr>)
```

## Exemplos do Analyze

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
INSTR(<str>, <substr>)
```

## Argumentos

| Argumentos | Descrição                |
|------------|--------------------------|
| `<str>`    | A cadeia de caracteres.  |
| `<substr>` | A subcadeia.             |

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

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
