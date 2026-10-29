---
title: CONCAT (Lakehouse v1)
description: CONCAT — devolve a cadeia de caracteres que resulta da concatenação dos argumentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

Devolve a cadeia de caracteres que resulta da concatenação dos argumentos. Pode ter um ou mais argumentos. Se todos os argumentos forem cadeias de caracteres não binárias, o resultado é uma cadeia de caracteres não binária. Se os argumentos incluírem alguma cadeia de caracteres binária, o resultado é uma cadeia de caracteres binária. Um argumento numérico é convertido na sua forma equivalente de cadeia de caracteres não binária.

## Sintaxe do Analyze

```python
func.concat(<expr1>, ...)
```

## Exemplos do Analyze

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## Sintaxe SQL

```sql
CONCAT(<expr1>, ...)
```

## Argumentos

| Argumentos | Descrição               |
|-----------|-------------------------|
| `<expr1>` | cadeia de caracteres    |

## Tipo de Retorno

Um valor do tipo de dados `VARCHAR` ou o tipo de dados `NULL`.

## Exemplos SQL

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
