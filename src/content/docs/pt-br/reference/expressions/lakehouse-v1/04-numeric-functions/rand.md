---
title: RAND() (Lakehouse v1)
description: RAND() — retorna um valor de ponto flutuante aleatório v no intervalo 0 <= v < 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

Retorna um valor de ponto flutuante aleatório v no intervalo 0 &lt;= v &lt; 1.0. Para obter um inteiro aleatório R no intervalo i &lt;= R &lt; j, use a expressão FLOOR(i + RAND() * (j − i)).

## Sintaxe do Analyze

```python
func.rand()
```

## Exemplos do Analyze

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## Sintaxe SQL

```sql
RAND()
```

## Exemplos de SQL

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
