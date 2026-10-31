---
title: CONCAT (Lakehouse v1)
description: CONCAT — retorna a string resultante da concatenação dos argumentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

Retorna a string resultante da concatenação dos argumentos. Pode ter um ou mais argumentos. Se todos os argumentos forem strings não binárias, o resultado será uma string não binária. Se os argumentos incluírem alguma string binária, o resultado será uma string binária. Um argumento numérico é convertido para sua forma equivalente de string não binária.

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

| Argumentos | Descrição |
|-----------|-------------|
| `<expr1>` | string      |

## Tipo de retorno

Um valor do tipo de dados `VARCHAR` ou `NULL`.

## Exemplos de SQL

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
