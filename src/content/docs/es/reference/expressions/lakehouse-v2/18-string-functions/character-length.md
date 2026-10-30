---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — Devuelve el número de caracteres de una cadena. Alias de `CHAR_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

Devuelve el número de caracteres de una cadena. Alias de `CHAR_LENGTH`.

## Sintaxis de Analyze

```python
func.character_length(<str>)
```

## Ejemplos de Analyze

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## Sintaxis de SQL

```sql
CHARACTER_LENGTH(<str>)
```

## Ejemplos de SQL

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
