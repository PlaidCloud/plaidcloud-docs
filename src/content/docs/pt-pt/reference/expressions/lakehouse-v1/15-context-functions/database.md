---
title: DATABASE (Lakehouse v1)
description: DATABASE — devolve o nome da base de dados atualmente selecionada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

Devolve o nome da base de dados atualmente selecionada. Se nenhuma base de dados estiver selecionada, esta função devolve `default`.

## Sintaxe do Analyze

```python
func.database()
```

## Exemplos do Analyze

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
