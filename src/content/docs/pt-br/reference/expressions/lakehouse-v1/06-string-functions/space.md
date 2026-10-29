---
title: SPACE (Lakehouse v1)
description: SPACE — retorna uma string formada por N caracteres de espaço em branco.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

Retorna uma string formada por N caracteres de espaço em branco.

## Sintaxe do Analyze

```python
func.space(<n>)
```

## Exemplos do Analyze

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## Sintaxe SQL

```sql
SPACE(<n>);
```

## Argumentos

| Argumentos | Descrição                |
|-----------|--------------------------|
| `<n>`     | O número de espaços      |

## Tipo de retorno

Valor do tipo de dados string.

## Exemplos de SQL

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
