---
title: TYPEOF (Lakehouse v1)
description: TYPEOF — a função TYPEOF é usada para retornar o nome de um tipo de dados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

A função TYPEOF é usada para retornar o nome de um tipo de dados.

## Sintaxe no Analyze

```python
func.typeof( <expr> )
```

## Exemplos no Analyze

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## Sintaxe SQL

```sql
TYPEOF( <expr> )
```

## Argumentos

| Argumentos  | Descrição   |
| ----------- | ----------- |
| `<expr>` | Qualquer expressão. <br /> Pode ser o nome de uma coluna, o resultado de outra função ou uma operação matemática.

## Tipo de retorno

String

## Exemplos de SQL

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
