---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — devolve o número de carateres de uma cadeia. Alias de `CHAR_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

Devolve o número de carateres de uma cadeia. Alias de `CHAR_LENGTH`.

## Sintaxe do Analyze

```python
func.character_length(<str>)
```

## Exemplos do Analyze

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## Sintaxe SQL

```sql
CHARACTER_LENGTH(<str>)
```

## Exemplos SQL

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
