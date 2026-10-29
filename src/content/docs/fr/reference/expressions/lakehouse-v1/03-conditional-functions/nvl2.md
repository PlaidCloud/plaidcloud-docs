---
title: NVL2 (Lakehouse v1)
description: NVL2 — renvoie <expr2> si <expr1> n'est pas NULL ; sinon, renvoie <expr3>.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nvl2.md
---

Renvoie `<expr2>` si `<expr1>` n'est pas NULL ; sinon, renvoie `<expr3>`.

## Syntaxe Analyze

```python
func.nvl2(<expr1> , <expr2> , <expr3>)
```

## Exemples Analyze

```python
func.nvl2('a', 'b', 'c'), func.nvl2(null, 'b', 'c')

┌──────────────────────────────────────────────────────┐
│ func.nvl2('a', 'b', 'c') │ func.nvl2(null, 'b', 'c') │
├──────────────────────────┼───────────────────────────┤
│ b                        │ c                         │
└──────────────────────────────────────────────────────┘

func.nvl2(1, 2, 3), func.nvl2(null, 2, 3)

┌────────────────────────────────────────────┐
│ func.nvl2(1, 2, 3) │ func.nvl2(null, 2, 3) │
├────────────────────┼───────────────────────┤
│                  2 │                     3 │
└────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
NVL2(<expr1> , <expr2> , <expr3>)
```

## Exemples SQL

```sql
SELECT NVL2('a', 'b', 'c'), NVL2(NULL, 'b', 'c');

┌────────────────────────────────────────────┐
│ nvl2('a', 'b', 'c') │ nvl2(null, 'b', 'c') │
├─────────────────────┼──────────────────────┤
│ b                   │ c                    │
└────────────────────────────────────────────┘

SELECT NVL2(1, 2, 3), NVL2(NULL, 2, 3);

┌──────────────────────────────────┐
│ nvl2(1, 2, 3) │ nvl2(null, 2, 3) │
├───────────────┼──────────────────┤
│             2 │                3 │
└──────────────────────────────────┘
```
