---
title: TYPEOF (Lakehouse v1)
description: TYPEOF es una función que se usa para devolver el nombre de un tipo de dato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

La función TYPEOF se usa para devolver el nombre de un tipo de dato.

## Sintaxis de Analyze

```python
func.typeof( <expr> )
```

## Ejemplos de Analyze

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## Sintaxis de SQL

```sql
TYPEOF( <expr> )
```

## Argumentos

| Argumentos  | Descripción |
| ----------- | ----------- |
| `<expr>` | Cualquier expresión. <br /> Puede ser el nombre de una columna, el resultado de otra función o una operación matemática.

## Tipo de retorno

Cadena

## Ejemplos de SQL

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
