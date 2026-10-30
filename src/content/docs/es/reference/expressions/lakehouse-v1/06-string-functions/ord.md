---
title: ORD (Lakehouse v1)
description: ORD — devuelve el código del carácter situado más a la izquierda de una cadena (valor ASCII para un solo byte, valor calculado para multibyte).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

Si el carácter situado más a la izquierda no es un carácter multibyte, ORD() devuelve el mismo valor que la función ASCII().

Si el carácter situado más a la izquierda de la cadena str es un carácter multibyte, devuelve el código de ese carácter,
calculado a partir de los valores numéricos de sus bytes constituyentes con esta fórmula:

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Sintaxis de Analyze

```python
func.ord(<str>)
```

## Ejemplos de Analyze

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## Sintaxis SQL

```sql
ORD(<str>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<str>`   | La cadena. |

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
