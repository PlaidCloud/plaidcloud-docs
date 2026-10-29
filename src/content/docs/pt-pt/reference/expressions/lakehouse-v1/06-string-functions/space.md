---
title: SPACE (Lakehouse v1)
description: SPACE — devolve uma cadeia de caracteres composta por N carateres de espaço em branco.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

Devolve uma cadeia de caracteres composta por N carateres de espaço em branco.

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

| Argumentos | Descrição              |
|-----------|------------------------|
| `<n>`     | O número de espaços    |

## Tipo de Retorno

Valor do tipo de dados cadeia de caracteres.

## Exemplos SQL

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
