---
title: RAND(n) (Lakehouse v1)
description: RAND(n) — retorna um valor de ponto flutuante aleatório v no intervalo 0 &lt;= v &lt; 1.0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

Retorna um valor de ponto flutuante aleatório v no intervalo 0 &lt;= v &lt; 1.0. Para obter um inteiro aleatório R no intervalo i &lt;= R &lt; j, use a expressão FLOOR(i + RAND() * (j − i)). O argumento `n` é usado como valor de semente. Para valores de argumento iguais, RAND(n) retorna o mesmo valor a cada vez e, portanto, produz uma sequência repetível de valores de coluna.

## Sintaxe do Analyze

```python
func.rand( <n>)
```

## Exemplos do Analyze

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## Sintaxe SQL

```sql
RAND( <n>)
```

## Exemplos de SQL

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
