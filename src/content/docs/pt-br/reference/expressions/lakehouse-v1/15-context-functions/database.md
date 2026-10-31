---
title: DATABASE (Lakehouse v1)
description: DATABASE — retorna o nome do banco de dados atualmente selecionado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

Retorna o nome do banco de dados atualmente selecionado. Se nenhum banco de dados estiver selecionado, a função retorna `default`.

## Sintaxe no Analyze

```python
func.database()
```

## Exemplos no Analyze

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## Sintaxe SQL

```sql
DATABASE()
```

## Exemplos de SQL

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
